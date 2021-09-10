from math import * #Import the math library to use pi
mass = 5.962 * pow(10, 24) #Kg
gravity = 6.67430 * pow(10, -11) #m^3.Kg^-1.s^-1
c = 299792458 #m/s

#The Schwarzschild Radius formula
def schwarzschild(gravity, mass, light):
	r = (2 * gravity * mass) / pow(light, 2)
	return r

#Calculate the volume of a sphere (in this case the Earth, compressed)
def volume(pi, radius):
	volume = (4/3) * pi * pow(radius, 3)
	return volume

radius = schwarzschild(gravity, mass, c)

print("Radius: " + str(radius * pow(10, 3)) + "mm" +"\nDiameter: " + str(radius * pow(10, 2) * 2) + "cm" + "\nVolume: " + str(volume(pi, radius * pow(10, 2))) + "cm3")