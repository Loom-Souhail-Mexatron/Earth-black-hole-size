from math import * #Import the math library to use pi
#mass = 5.962 * pow(10, 24) in Kg, the mass of Earth
gravity = 6.67430 * pow(10, -11) #m^3.Kg^-1.s^-1
c = 299792458 #m/s

#Masses of different planets in our solar system and the sun
masses = {
	"Sun" 	  : 1.989 * pow(10, 30),
	"Mercury" : 3.285 * pow(10, 23),
	"Venus"	  : 4.867 * pow(10, 24),
	"Earth"	  : 5.962 * pow(10, 24),
	"Mars"	  : 6.390 * pow(10, 23),
	"Jupiter" : 1.898 * pow(10, 27),
	"Saturn"  : 5.683 * pow(10, 26),
	"Uranus"  : 8.681 * pow(10, 25),
	"Neptune" : 1.024 * pow(10, 26)
}
	
#The Schwarzschild Radius formula
def schwarzschild(gravity, mass, light):
	r = (2 * gravity * mass) / pow(light, 2)
	return r

#Calculate the volume of a sphere (in this case the Earth, compressed)
def volume(pi, radius):
	volume = (4/3) * pi * pow(radius, 3)
	return volume

#Calculates schwarzschild radius for Earth
#radius = schwarzschild(gravity, mass, c)

for planet in masses:
    print(planet)
    radius = schwarzschild(gravity, masses[planet], c)
    print("Radius: " + str(radius * pow(10, 3)) + "mm")
    print("Diameter: " + str(radius * pow(10, 2) * 2) + "cm")
    print("Volume: " + str(volume(pi, radius * pow(10, 2))) + "cm3")
    print(" ")
