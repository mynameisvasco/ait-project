from fcm import Fcm

fcm = Fcm(0.01, 3)
fcm.add_file("example/example.txt")

assert fcm.smoothing == 0.01
assert fcm.context_size == 3
assert fcm.get_symbol_probability(" ", "the") == 0.5803758789221616
assert fcm.get_model_entropy() == 1.9974842229594973
