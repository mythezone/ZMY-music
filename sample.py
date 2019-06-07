from music21 import *

noteList = []

# from note name
n = note.Note("F#4",quarterLength = 1)
noteList.append(n)

# from pitch with note name
p = pitch.Pitch("F#4")
n = note.Note(pitch=p,quarterLength = 1)
noteList.append(n)

# from midi note F#4=66
curnote = 66 
n = note.Note(midi=curnote,quarterLength = 1)
noteList.append(n)

# deep copy
n2 = note.Note(n.pitch,quarterLength=n.quarterLength)
noteList.append(n2)

meas = stream.Measure()
meas.append(noteList)

meas.show('musicxml')