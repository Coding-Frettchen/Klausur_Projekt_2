Farben_Auto = [ "gruen" , "gelb", "rot", "rot+gelb", "Blinken"]
Farben_Fuß = ["gruen", "rot", "aus"]
night = true

class Auto_Apmel(object):
     zustand = 0
     Start_pose = 0
     def __init__(self, Start_pos):
	zustand = Start_pos
	Start_pose = Start_pos
	self.Farbe = Farben[Start_pos]

     def schalten(self):
	if night == true:
	  self.Farbe = Farben[4]
	elif night == false:
	  self.Farbe = Farben[Start_pose]
	elif zustand = 3:
	  zustand = 0
	else:
	 zustand += 1

     def update(self):
	self.Farbe = Farben[zustand]


