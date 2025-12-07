from threading import Thread, Event
import random
from time import sleep
Farben_Auto = [ "gruen" , "gelb", "rot", "rot+gelb", "Blinken"]
Farben_Fuß = ["gruen", "rot", "aus"]
night = True
tick_auto = Event()
tick_fuß = Event()

class Auto_ampel(object):
	def __init__(self, Start_pose):
		self.zustand = Start_pose
		self.Start_pos = Start_pose
		self.Farbe = Farben_Auto[Start_pose]
		self.update_thread = Thread(target=self.update)
		self.schalten_thread = Thread(target=self.auto_schalten)
		self.beat_thread = Thread(target=self.schalt_beat)
		self.update_thread.start()
		self.schalten_thread.start()
		self.beat_thread.start()

	def schalten(self):
		if night:
			self.Farbe = self.zustand(4)
			return

		if self.zustand == 3:
			self.zustand = 0
		else:
			self.zustand += 1

	def auto_schalten(self):
		while True :
			tick_auto.wait()
			tick_auto.clear()
			self.schalten()

	def schalt_beat(self):
		while True:
			sleep(2)
			sleep(random.uniform(0.0002, 0.0005))
			tick_auto.set()

	def update(self):
		while True:
			self.Farbe = Farben_Auto[self.zustand]
			sleep(0.5)



class Fuß_ampel(object):

	def __init__(self, Start_pose):
		self.zustand = Start_pose
		self.Start_pos = Start_pose
		self.Farbe = Farben_Fuß[Start_pose]
		self.update_thread = Thread(target=self.update)
		self.schalten_thread = Thread(target=self.auto_schalten)
		self.beat_thread = Thread(target=self.schalt_beat)
		self.update_thread.start()
		self.schalten_thread.start()

	def auto_schalten(self):
		while True :
			tick_fuß.wait()
			tick_fuß.clear()
			self.schalten()

	def schalt_beat(self):
		while True:
			sleep(4)
			sleep(random.uniform(0.0002, 0.0005))
			tick_fuß.set()


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
	inti_art = input("Ampel Initialsierung Art ('A' für Automatisch; 'M' für Manuel): ")
	if inti_art == "A":
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
			startzustand = int(input(f"{Name_ampel}s Start Position ('0' für gruen, '2' für rot): "))
			Name_ampel = Auto_ampel(startzustand)
		for _ in range(4): 
			Name_ampel = input(f"Name der Fuß_Ampel_{_+1}: ")
			startzustand = int(input(f"{Name_ampel}s Start Position ('0' für gruen. '1' für rot): "))
			Name_ampel = Fuß_ampel(startzustand)
user_interface()

