from numpy import loadtxt
from numpy import savetxt

arq = 'R5_6 - N 5184.txt'

m = loadtxt(arq, dtype = int)

m = m.reshape((4, 24), order = 'F')

savetxt(arq, m, fmt='%d' ,comments="# matriz H LDPC com taxa 5/6 e N 5184, t = 24, c = 4")