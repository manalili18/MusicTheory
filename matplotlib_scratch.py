#!/usr/bin/python

# takes in a freq, outputs the fft and some harmonics

import matplotlib.pyplot as plt
import numpy
import sys

freq1 = float(sys.argv[1])
intensity0 = 1.0
num_harms = 10

tet_12 = 2.0 ** (1.0/12.0)

lowest_freq = 13.75

graph_dict = {}
graph_dict[lowest_freq] = 0.0



cur_freq = lowest_freq
highest_audible_freq = 20000

while cur_freq < highest_audible_freq:
    cur_freq *= tet_12
    graph_dict[round(cur_freq,5)] = 0.0
    

#print(graph_dict)



# init freqs and intensity


def calc_harms(freq):
    freqs = []
    intensity = []
    for n in range(num_harms):
        freqs += [round(freq * (n+1),5)]
        intensity += [intensity0 / (n+1)]

    return freqs, intensity

add_x, add_y = calc_harms(freq1)

#update dictionary

def find_nearest(array, value):
    np_array = numpy.asarray(array)
    idx = (numpy.abs(np_array - value)).argmin()
    return np_array[idx]

for freq, intensity in zip(add_x,add_y):
    nearest_freq = find_nearest(sorted(graph_dict.keys()),freq)
    graph_dict[nearest_freq] += intensity 

print(graph_dict)

x = []
y = []

for key in sorted(graph_dict.keys()):
    x += [key]
    y += [graph_dict[key]]
    
plt.plot(x,y)

plt.show()


#plt.plot(x,y)
#plt.show()

