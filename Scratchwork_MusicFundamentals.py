# Author's note:
#   Most of this code is irrelevant and can be solved much faster by
#   simply writing out the result as the end goal (a list of tuples)
#   but this has been a good warm up for list manipulation for me,
#   and I will leave it in.
#
#   Also, most of this code is a study exercise to help me understand
#   the relationship that coding has with music theory.

cur_char = 'A'
naturals = []
sharps = []
flats = []

for i in range(7):
  naturals = naturals + [(chr(ord(cur_char)+i))]

for i in range(7):
  sharps = sharps + [(chr(ord(cur_char)+i)+"#")]
print()

for i in range(7):
  flats = flats + [(chr(ord(cur_char)+i)+"b")]

# zipping lists and returning list
#[item for pair in zip(a, b) for item in pair]

sharps =  [item for pair in zip(naturals, sharps) for item in pair]
flats =  [item for pair in zip(flats, naturals) for item in pair]

# remove unnecessary enharmonics
sharps.remove('B#')
sharps.remove('E#')
flats.remove('Cb')
flats.remove('Fb')

# cycle the list
flats.append(flats.pop(0))

enharmonics = [(sharp,flat) for sharp,flat in zip(sharps,flats)]

# TODO sharp or flat decider

# cycle the list 3 times
for i in range(3):
  enharmonics.append(enharmonics.pop(0))
  flats.append(flats.pop(0))
  sharps.append(sharps.pop(0))


# function for printing chords
def tetrachord(scale, index):
  # I could use an itertools cycle, AND it would be SUPER useful in the future
  # but I am lazy, and I need instant gratification right now for some reason
  #  17 January 2020

  # scale is list
  unison = scale[index]
  third = scale[(index+2)%12]
  fifth = scale[(index+4)%12]
  seventh = scale[(index+6)%12]

  return (unison, third, fifth, seventh)

# produces an ionian scale given the chordtone
def ionian(note):
  unison = sharps.index(note)
  maj_sec = sharps[((unison+2)%12)]
  maj_thr = sharps[((unison+4)%12)]
  per_for = sharps[((unison+5)%12)]
  per_fif = sharps[((unison+7)%12)]
  maj_six = sharps[((unison+9)%12)]
  maj_sev = sharps[((unison+11)%12)]
  unison = sharps[((unison)%12)]

  scale = (unison, maj_sec, maj_thr, per_for, per_fif, maj_six, maj_sev)

  return scale
  


# TODO Objectify everything
### DEBUGGING PRINTS BELOW THIS LINE ###

for note in sharps:
  print(ionian(note))

print(enharmonics)
print(sharps)
print(flats)


