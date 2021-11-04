from fcm import Fcm
from generator import Generator

fcm = Fcm(0.10, 4)
fcm.add_file("example/maias.txt")
fcm.add_file("example/crimepadreamaro.txt")
fcm.add_file("example/mandarim.txt")

generator = Generator(fcm)
generated_text = generator.generate("ola ", 255)

assert len(generated_text) == 255
assert "ola" in generated_text
