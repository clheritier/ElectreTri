from functions_electre import *
from input_checking import *
from functions_contribution import *
import numpy as np

""" Electre tri with with pessimistic procedure: assign 'a' to one of the p predefined categories (delimited with profiles bh)
    In this version parameters may be provided directly (no input fct used). 
    Parameters to provide depend on the nb of categories and then nb of profiles. 
    /!\ performance on criteria is supposed to be croissant (if not, the performance gj must be negative)
    Parameters are the following:
        p = nb of predefined categories                     int>1
        n = nb of criteria                                  int>0
        cut_level = cutting level                           float in [0.5,1]
        w = weight vector                                   w = np.array([w1, ..., wj, ..., wn]
        a = performance vector of 'a'                       a = np.array([g1(a), ..., gj(a), ..., gn(a)])
      For all h in {1,..p-1}
        b[h] = performance vector of profile 'bh'           b[h] = np.array([g1(bh), ..., gj(bh), ..., gn(bh)])
        qb[h] = vector of indifference threshold  for bh    qb[h] = np.array([q(g1(bh)), ....., q(gn(bh))])
        pb[h] = vector of preference threshold  for bh      pb[h] = np.array([p(g1(bh)), ....., p(gn(bh))])
        vb[h] = vector of veto threshold  for bh            vb[h] = np.array([v(g1(bh)), ....., v(gn(bh))])
        """

### PARAMETERS TO PROVIDE 1/2
p = 3
n = 8
w = np.array([11.28,41.7,14.9,5.77,7.84,4.06,7.86,17])
cut_level = 0.93
a = np.array([-22,88,-52,-30,2,4,2,4])

### /!\ do not modify
h= p-1
b = np.empty((h,n))
qb = np.empty((h,n))
pb = np.empty((h,n))
vb = np.empty((h,n))

### PARAMETERS TO PROVIDE 2/2
b[0] = np.array([-26,63,-53,-81,2,2,2,3])
b[1] = np.array([-7,96,-34,-47,3,3,3,3])
qb[0] = np.array([3,3,2,7,0,0,0,0])
qb[1] = np.array([5,8,4,3,0,0,0,0])
pb[0] = np.array([10,7,6,14,1,1,1,1])
pb[1] = np.array([10,10,7,6,1,1,1,1])
vb[0] = np.array([80,40,70,200,3,2,2,3])
vb[1] = np.array([80,40,70,200,3,2,2,3])


###
approx = False
approx = input_bool("Use approximation for cj: yes/no ?")

###
cj_ab = np.empty((0, n))
C_ab = []
dj_ab = np.empty((0, n))
rho_ab = []
ab=[]

### 1|Use function electre_3 to compute partial concordance,comprehensive concordance, discordance, credibility,
# outranking for pairs (a,bh) for all h in {1,..,p-1}

for i in range(0,h,1):
    abi = electre_3(a,b[i],qb[i],pb[i],vb[i],w,cut_level,approx)
    ab.append(abi)

for i in range(0,h,1):
        print("\n # Partial concordance indices:\n "
              "\t c(a,b{0})={1}\n "
              "# Comprehensive concordance index: \n"
              "\t C(a,b{0})={2}\n "
              " # Discordance indices: \n "
              "\t d(a,b{0})={3}\n "
              "# Credibility index: \n "
              "\t rho(a,b{0})={4}\n "
              "# Outranking with lambda ={5}\n"
              "\t aSb{0} = {6}\n"
              "_________________________________"
              .format((i+1),ab[i][0],ab[i][1],ab[i][2], ab[i][3], cut_level, ab[i][4]))

        # indices 0 to 4, allow to gat the 5 elements contained in the list returned with function electre_3
        #note: if h=2, results are expected for (a,b1) and (a,b2), thus list ab has the following form:
        # ab = [[array1], [array2]]
        # ab = [[[cj(a,b1)], C(a,b1), [dj(a,b1)], rho(a,b1), boolean],
        #       [[cj(a,b2)], C(a,b2), [dj(a,b2)], rho(a,b2), boolean]]]
        # boolean => true means aSb, False means not(aSb)

### 2| Assignment procedure (pessimistic)

for i in range(h,0,-1):
    if ab[i-1][4] == True:   #return boolean S(a,bh) True/false
        print("\n The pessimistic procedure assigns 'a' to category C{}".format((i+1)))
        r = i-1 # return index of profile br such as aSbr
        break
else:
    print("The pessimistic procedure assigns 'a' to category C1 \n") ## on supppose que a surclasse forcement b0
    r=0
    # , et par defaut assigne a la moins bonne des cate c0

### 3| Contribution

#/!\ if r != -1: # si surclasse profils b0 avec pessimitic procedure, il faudra regarder pourquoi b1Sa

cj_abr = ab[r][0]*w/np.sum(w)
lambda_abr = function_lambda_abr(cut_level, ab[r][2] , ab[r][1])


print("\n Individual contributions c{j}(a,br): \n c{j}(a,b",r+1,")=",cj_abr)
print("\n The cutting level lambda =", cut_level)
print(" Threshold lambda(a,br) = ",lambda_abr)
gamma_ = input_gamma(" Enter threshold 'gamma' such that the individual contribution of each criterion of I should exceed this minimal value, gamma in ]0,1]")

