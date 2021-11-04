from fcm import Fcm
from generator import Generator

fcm = Fcm(0.01, 3)
fcm.add_file("example/example.txt")
generator = Generator(fcm)

assert fcm.smoothing == 0.01
assert fcm.context_size == 3
print(fcm.get_symbol_probability(" ", "the"))
# assert fcm.get_symbol_probability(" ", "the") == 0.5803758789221615
# assert fcm.get_model_entropy() == 1.9974842229594973

print(generator.generator('The ', 30))
