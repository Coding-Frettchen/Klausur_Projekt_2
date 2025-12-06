from threading import Thread
from time import sleep
Farben_Auto = [ "gruen" , "gelb", "rot", "rot+gelb", "Blinken"]
Farben_Fuß = ["gruen", "rot", "aus"]
night = True

class Auto_ampel(object):
	def __init__(self, Start_pose):
		self.zustand = Start_pose
		self.Start_pos = Start_pose
		self.Farbe = Farben_Auto[Start_pose]
		self.update_thread = Thread(target=self.update(self))
		self.update_thread.start()

	def schalten(self):
		if night == True:
			self.Farbe = Farben_Auto[4]
		elif night == False:
			self.Farbe = Farben_Auto[self.Start_pos]
		elif self.zustand == 3:
			self.zustand = 0
		else:
			self.zustand += 1

	def update(self):
		while True:
			self.Farbe = Farben_Auto[self.zustand]
			sleep(0.5)


class Fuß_ampel(object):

	def __init__(self, Start_pose):
		self.zustand = Start_pose
		self.Start_pos = Start_pose
		self.Farbe = Farben_Fuß[Start_pose]
		self.update_thread = Thread(target=self.update(self))
		self.update_thread.start()

	def schalten(self):
		if self.zustand == 2:
			self.zustand = 0
		else:
			self.zustand += 1

	def update(self):
		while True:
			self.Farbe = Farben_Fuß[self.zustand]
			sleep(0.5)

def user_interface():
	inti_art = input("Ampel Initialsierung Art (ENTER oder 'A' für Automatisch; 'M' für Manuel): ")
	if inti_art == "A" or None:
		Ampel_A_Nord_Süd = Auto_ampel(0)
		Ampel_A_Süd_Nord = Auto_ampel(0)
		Ampel_A_Ost_West = Auto_ampel(2)
		Ampel_A_West_Ost = Auto_ampel(2)
		Ampel_F_Nord_Süd = Fuß_ampel(1)
		Ampel_F_Süd_Nord = Fuß_ampel(1)
		Ampel_F_West_Ost = Fuß_ampel(0)
		Ampel_F_Ost_West = Fuß_ampel(0)
	elif inti_art == "M":
		for _ in range(4): 
			Name_ampel = input(f"Name der Auto_Ampel_{_+1}: ")
			startzustand = input(f"{Name_ampel}s Start Position ('0' für gruen, '2' für rot): ")
			Name_ampel = Auto_ampel(startzustand)
		for _ in range(4): 
			Name_ampel = input(f"Name der Fuß_Ampel_{_+1}: ")
			startzustand = input(f"{Name_ampel}s Start Position ('0' für gruen. '1' für rot): ")
			Name_ampel = Fuß_ampel(startzustand)
user_interface()