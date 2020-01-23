#!/usr/bin/python

# again this is scratchwork to help promote my understanding of music
# these values generated by this program are easily found on the internet
# but I will be deriving them starting from A = 440 Hz because I find value
# from understanding this process from the ground up

# this program will generate valid notes from 20 Hz to 20 kHz

# start with the 12 valid notes using 12-TET 
start = 'A'

chromatic_sharps = []

for i in range(7):
    chromatic_sharps.append(chr(ord(start)+i))
    chromatic_sharps.append(chr(ord(start)+i)+'#')

chromatic_sharps.remove('B#')
chromatic_sharps.remove('E#')


chromatic_flats = []

for i in range(7):
    chromatic_flats.append(chr(ord(start)+i)+'b')
    chromatic_flats.append(chr(ord(start)+i))

chromatic_flats.remove('Cb')
chromatic_flats.remove('Fb')

chromatic_flats.append(chromatic_flats.pop(0))

tuning_system = 2.0 ** (1.0/12.0)

notes_hz_sharps = {}
notes_hz_flats = {}

base_hz_sharps = {}
base_hz_flats = {}

a440 = 440.0

for sharp, flat, i in zip(chromatic_sharps, chromatic_flats, range(len(chromatic_sharps))):
    hz = a440 * (tuning_system ** i)
    notes_hz_sharps[sharp] = hz
    notes_hz_flats[flat] = hz
    
    cur_base_hz = hz

    while cur_base_hz >= 40:
        cur_base_hz /= 2
        
    base_hz_sharps[sharp] = cur_base_hz
    base_hz_flats[flat] = cur_base_hz

note_freq = {}

for note in base_hz_flats:
    cur_freq = base_hz_flats[note]
    cur_note_freqs = []
    while cur_freq < 20000:
        cur_note_freqs += [cur_freq]
        cur_freq *= 2

    note_freq[note] = cur_note_freqs

    
notes_sorted = ['E','F','Gb','G','Ab','A','Bb','B','C','Db','D','Eb']

# invert dictionary
freq_note = {}
for note in note_freq:
    for freq in note_freq[note]:
        freq_note[freq] = note

# add octave count and #print

cur_octave = 0

for freq in sorted(freq_note.keys()):
    cur_octave += 1 if freq_note[freq] == 'C' else 0
    freq_note[freq] = freq_note[freq] + str(cur_octave)
    formatted_line = str(freq_note[freq])+'\t'+str(freq)
    #print(formatted_line)


def harmonic_series(fundamental):
    return -1
    
    


