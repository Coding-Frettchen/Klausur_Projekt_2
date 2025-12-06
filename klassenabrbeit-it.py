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


