from fcm import Fcm
from generator import Generator

fcm = Fcm(0.10, 4)
fcm.add_file("example/maias.txt")
fcm.add_file("example/crimepadreamaro.txt")
fcm.add_file("example/mandarim.txt")

generator = Generator(fcm)
print(generator.generator(input("Prior: "), 255))
