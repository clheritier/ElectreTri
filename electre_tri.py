


from functions_electre import*
import numpy as np
from input_checking import*

"""
    w: weight
    p: 
    h:
    n:
    """

#############################################################
#         INPUT MODEL PARAMETERS
#############################################################


## define number p of categories and check if p is an integer
p = input_int_positif("Enter the number p of predefined categories: ")
h = p-1 #profil bh to define
print("--> Cp categories, p = 1,..,{} , and \n"
      "--> bh profiles to define, h = 1,..,p-1, bh being the upper profile of Ch and lower profile of Ch+1. \n".format(p))

# def criteria, weights, lambda, alternative a to assign
n = input_int_positif("enter the number of criteria: ")
w = input_array("Enter the weights coefficients (values separated with ','): ", n)

cut_level = input_lambda("Enter value of the cutting level lambda: ")

a = input_array("Enter the performance vector g(a) \n (values separated with ','): ",n)

### definir les profils bh

b = np.empty((0,n))
for i in range(1,p,1):
    new_row = input_array("enter profile b{}: ".format(i), n)
    b = np.append(b, [new_row],0)
#for i in range(1,p,1):
    #print("\n profile b{} = {} ".format(i, b[i-1]))

### definir les seuils q(g(bh))
qb = np.empty((0, n))
for i in range(1,p,1):
    new_row = input_array("enter indifference threshold vector q(g({})): ".format(i), n)
    qb = np.append(qb, [new_row],0)


### definir les seuils p(g(bh))
pb = np.empty((0, n))
for i in range(1,p,1):
    new_row = input_array("enter preference threshold vector p(g(b{})): ".format(i), n)
    pb = np.append(pb, [new_row],0)


### definir les seuils v(g(bh))
vb = np.empty((0, n))
for i in range(1,p,1):
    new_row = input_array("enter veto threshold vector v(g(b{})): ".format(i), n)
    vb = np.append(vb, [new_row],0)


#### print model input parameters #####

print("--> Cp categories, p = 1,..,{} , and \n"
      "--> bh profiles to define, h = 1,..,p-1, bh being the upper profile of Ch and lower profile of Ch+1. \n".format(p))

print("alternatives are evaluated on n={} criteria, \n and importance coefficient defined by the vector w = {}\n".format(n,w))
print("the cutting level is lambda = {} \n".format(cut_level))

print("The alternative a to assigned is defined with performance vector: \n g(a)= {} \n".format(a))

print("predefined categories profiles are defined as follow: ")
for i in range(1,p,1):
    print("\n b{} = \t{} \n"
          " q(g({})) = \t{} \n"
          " p(g({})) = \t{} \n"
          " v(g({})) = \t{}".format(i, b[i-1],i, qb[i-1],i, pb[i-1],i, vb[i-1]))



#############################################################
#       RUN ELECTRE TRI TO ASSIGN ALTERNATIVE 'a'
#############################################################

approx = input_bool("Use approximation for cj: yes/no ?")

### partial concordance
cj_ab = np.empty((0, n))
for i in range(1,p,1):
    if approx == false:
        new_row = partial_concordance(a, b[i-1], qb[i-1], pb[i-1])
        cj_ab = np.append(cj_ab, [new_row],0)
    else:
        new_row = partial_concordance_approx(a, b[i - 1], qb[i - 1], pb[i - 1])
        cj_ab = np.append(cj_ab, [new_row], 0)

for i in range(1,p,1):
    print("partial concordance indices: \n"
          " c(a,b{}) = {}\n".format(i, cj_ab[i-1]))

### comprhensive concordance
C_ab = np.empty((0,1))
for i in range(1,p,1):
    new_row = comprehensive_concordance(cj_ab[i-1], w)
    C_ab = np.append(C_ab, [new_row], 0)
    print("partial concordance indices: \n"
          " C(a,b{}) = {}\n".format(i, C_ab[i - 1]))


### discordance
dj_ab = np.empty((0, n))
for i in range(1,p,1):
        new_row = discordance(a, b[i-1], pb[i-1], vb[i-1])
        dj_ab = np.append(dj_ab, [new_row],0)

for i in range(1,p,1):
    print("discordance indices: \n"
          " d(a,b{}) = {}\n".format(i, dj_ab[i-1]))

### credibility
rho_ab = np.empty((0,1))
for i in range(1,p,1):
    new_row = credibility(C_ab[i-1], dj_ab[i-1])
    rho_ab = np.append(rho_ab, [new_row], 0)
    print("partial concordance indices: \n"
          " rho(a,b{}) = {}\n".format(i, rho_ab[i - 1]))