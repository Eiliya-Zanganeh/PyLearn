import pysynth as ps

notes = [('c', 4), ('d', 4), ('e', 4), ('f', 4), ('g', 4), ('a', 4), ('b', 4)]
ps.make_wav(notes, fn = "test.wav")