import tkinter as tk
import ampel_core  # ampel_core.py liegt im gleichen Ordner

# Nachtmodus im Core sicherheitshalber aus
ampel_core.night = False

# -----------------------
# Ampeln erzeugen (Core bleibt unverändert)
# -----------------------
A_NS = ampel_core.Auto_ampel(0)  # Auto Nord -> Süd
A_SN = ampel_core.Auto_ampel(0)  # Auto Süd -> Nord (für Logik vorhanden, im UI gespiegelt)
A_OW = ampel_core.Auto_ampel(2)  # Auto Ost -> West
A_WO = ampel_core.Auto_ampel(2)  # Auto West -> Ost (für Logik vorhanden, im UI gespiegelt)

F_NS = ampel_core.Fuß_ampel(1)
F_SN = ampel_core.Fuß_ampel(1)
F_WO = ampel_core.Fuß_ampel(0)
F_OW = ampel_core.Fuß_ampel(0)


# -----------------------
# Hilfsfunktionen: Farben mappen
# -----------------------

def auto_to_color_tuple(farbe: str):
    """Gibt (rot, gelb, gruen) als Farbstrings zurück."""
    if farbe == "gruen":
        return "grey", "grey", "green"
    if farbe == "gelb":
        return "grey", "yellow", "grey"
    if farbe == "rot":
        return "red", "grey", "grey"
    if farbe == "rot+gelb":
        return "red", "yellow", "grey"
    if farbe == "Blinken":
        # gelb blinkend -> statisch gelb anzeigen
        return "grey", "yellow", "grey"
    return "grey", "grey", "grey"


def fuss_to_color_tuple(farbe: str):
    """Fußgänger: (rot, gruen), 'aus' wird als rot angezeigt, damit nie alles dunkel ist."""
    if farbe == "gruen":
        return "grey", "green"
    if farbe == "rot":
        return "red", "grey"
    if farbe == "aus":
        # Fix: niemals komplett dunkel -> zeig rot
        return "red", "grey"
    return "grey", "grey"


# -----------------------
# View-Klassen
# -----------------------

class AutoView(tk.Frame):
    def __init__(self, master, get_farbe_callable, title: str):
        super().__init__(master)
        self.get_farbe = get_farbe_callable

        tk.Label(self, text=title, font=("Arial", 10, "bold")).pack()
        self.canvas = tk.Canvas(self, width=60, height=150)
        self.canvas.pack()

        self.red = self.canvas.create_oval(10, 5, 50, 45)
        self.yellow = self.canvas.create_oval(10, 55, 50, 95)
        self.green = self.canvas.create_oval(10, 105, 50, 145)

    def refresh(self):
        farbe = self.get_farbe()
        r, y, g = auto_to_color_tuple(farbe)
        self.canvas.itemconfig(self.red, fill=r)
        self.canvas.itemconfig(self.yellow, fill=y)
        self.canvas.itemconfig(self.green, fill=g)


class FussView(tk.Frame):
    def __init__(self, master, get_farbe_callable, title: str):
        super().__init__(master)
        self.get_farbe = get_farbe_callable

        tk.Label(self, text=title, font=("Arial", 10, "bold")).pack()
        self.canvas = tk.Canvas(self, width=60, height=100)
        self.canvas.pack()

        self.red = self.canvas.create_oval(10, 5, 50, 45)
        self.green = self.canvas.create_oval(10, 55, 50, 95)

    def refresh(self):
        farbe = self.get_farbe()
        r, g = fuss_to_color_tuple(farbe)
        self.canvas.itemconfig(self.red, fill=r)
        self.canvas.itemconfig(self.green, fill=g)


# -----------------------
# Fenster + Layout
# -----------------------

root = tk.Tk()
root.title("Ampel UI – Fix Version")

# Kreuzungs-Layout für Autos
auto_frame = tk.Frame(root)
auto_frame.pack(side=tk.LEFT, padx=20, pady=20)

# Wichtig: UI-Sync
# N->S und S->N zeigen die gleiche Farbe (A_NS)
# O->W und W->O zeigen die gleiche Farbe (A_OW)

auto_views = [
    AutoView(auto_frame, lambda: A_NS.Farbe, "Auto N→S"),
    AutoView(auto_frame, lambda: A_NS.Farbe, "Auto S→N"),
    AutoView(auto_frame, lambda: A_OW.Farbe, "Auto O→W"),
    AutoView(auto_frame, lambda: A_OW.Farbe, "Auto W→O"),
]

# Anordnung im Grid (Kreuzung)
auto_views[0].grid(row=0, column=1, padx=20, pady=20)  # N->S oben
auto_views[1].grid(row=2, column=1, padx=20, pady=20)  # S->N unten
auto_views[2].grid(row=1, column=0, padx=20, pady=20)  # O->W links
auto_views[3].grid(row=1, column=2, padx=20, pady=20)  # W->O rechts

# Fußgänger rechts daneben
fuss_frame = tk.Frame(root)
fuss_frame.pack(side=tk.RIGHT, padx=20, pady=20)

fuss_views = [
    FussView(fuss_frame, lambda: F_NS.Farbe, "Fuß N→S"),
    FussView(fuss_frame, lambda: F_SN.Farbe, "Fuß S→N"),
    FussView(fuss_frame, lambda: F_WO.Farbe, "Fuß W→O"),
    FussView(fuss_frame, lambda: F_OW.Farbe, "Fuß O→W"),
]

for v in fuss_views:
    v.pack(pady=10)


# -----------------------
# Update-Loop
# -----------------------

def refresh_all():
    # Alle Views aktualisieren
    for v in auto_views:
        v.refresh()
    for v in fuss_views:
        v.refresh()
    # alle 150 ms
    root.after(150, refresh_all)


refresh_all()
root.mainloop()
