from numpy import loadtxt
from numpy import savetxt

arq = 'R5_6 - N 5184.txt'

m = loadtxt(arq, dtype = int)

m = m.reshape((4, 24), order = 'F') #configurar o shape da matriz

savetxt(arq, m, fmt='%d' ,comments="# matriz H LDPC com taxa x/x e N xxx, t = xx, c = xx")