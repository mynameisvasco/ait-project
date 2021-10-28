from fcm import Fcm

fcm = Fcm(0.01, 3)
fcm.add_text("ababababa")

assert fcm.smoothing == 0.01
assert fcm.context_size == 3
assert fcm.get_all_contexts() == set((('a', 'b', 'b'), ('a', 'b', 'a'), ('b', 'b', 'b'), ('b', 'a', 'b'),
                                      ('b', 'b', 'a'), ('b', 'a', 'a'), ('a', 'a', 'b'), ('a', 'a', 'a')))


fcm = Fcm(0.01, 3)
hash = fcm.add_file("example/example.txt")
assert fcm.get_probability(" ", "the") == 0.5803758789221615
