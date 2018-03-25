from functions_electre import *
from input_checking import *
import numpy as np

###
p = 3
h = p-1
n = 8
w = np.array([11.28,41.7,14.9,5.77,7.84,4.06,7.86,17])
cut_level=0.93
a = np.array([-22,88,-52,-30,2,4,2,4])
###
b = np.empty((2,n))
qb = np.empty((2,n))
pb = np.empty((2,n))
vb = np.empty((2,n))

###
b[0] = np.array([-26,63,-53,-81,2,2,2,3])
b[1] = np.array([-7,96,-34,-47,3,3,3,3])
qb[0] = np.array([3,3,2,7,0,0,0,0])
qb[1] = np.array([5,8,4,3,0,0,0,0])
pb[0] = np.array([10,7,6,14,1,1,1,1])
pb[1] = np.array([10,10,7,6,1,1,1,1])
vb[0] = np.array([80,40,70,200,3,2,2,3])
vb[1] = np.array([80,40,70,200,3,2,2,3])
###


cj_ab = np.empty((0, n))
C_ab = []
dj_ab = np.empty((0, n))
rho_ab = []
#ab = np.empty((5, n))

ab=[]
for i in range(0,h,1):
    abi = electre_3(a,b[i],qb[i],pb[i],vb[i],w,cut_level)
    ab.append(abi)

for i in range(0,h,1):
    print(ab[i])



print(un[4])

#print("partial concordance indices\n "
#      "c(a,b{0})={1}\n"
 #     "comprehensive concordance index \n "
  #    "C(a,b{0})={2}\n"
  #    "discordance indices \n "
  #    "d(a,b{0})={3}\n"
  #    "credibility index \n "
  #    "rho(a,b{0})={4}\n"
  #    "outranking with lambda ={5}\n"
  #    "aSb{0} = {6}".format((i+1),ab[i],ab[i],ab[i], ab[i], cut_level, ab[i]))



#print(ab)

  #new_row = electre_3(a,b[i],qb[i],pb[i],vb[i],w[i],cut_level)
  #ab = np.append(ab, new_row),0)



