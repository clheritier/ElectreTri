


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
cut_level = input_lambda("Enter value of the cutting level lambda: ")
w = input_array("Enter the weights coefficients (values separated with ','): ", n)
a = input_array("Enter the performance vector g(a), (values separated with ','): ",n)

### define profiles bh

b = np.empty((0,n))
for i in range(0,h,1):
    new_row = input_array("Enter profile b{}: ".format(i+1), n)
    b = np.append(b, [new_row],0)


### define threholds q(g(bh))
qb = np.empty((0, n))
for i in range(0,h,1):
    new_row = input_array("Enter indifference threshold vector q(g({})): ".format(i+1), n)
    qb = np.append(qb, [new_row],0)


### define thresholds p(g(bh))
pb = np.empty((0, n))
for i in range(0,h,1):
    new_row = input_array("enter preference threshold vector p(g(b{})): ".format(i+1), n)
    pb = np.append(pb, [new_row],0)


### define threshold v(g(bh))
vb = np.empty((0, n))
for i in range(0,h,1):
    new_row = input_array("enter veto threshold vector v(g(b{})): ".format(i+1), n)
    vb = np.append(vb, [new_row],0)


#### print model input parameters #####

print("--> Cp categories, p = 1,..,{} , and \n"
      "--> bh profiles to define, h = 1,..,p-1, bh being the upper profile of Ch and lower profile of Ch+1. \n".format(p))

print("Alternatives are evaluated on n={} criteria, \n and importance coefficient defined by the vector w = {}\n".format(n,w))
print("The cutting level is lambda = {} \n".format(cut_level))

print("The alternative 'a' to assigned is defined with performance vector: \n g(a)= {} \n".format(a))

print("Predefined categories profiles are defined as follow: ")
for i in range(0,h,1):
    print("\n b{} = \t{} \n"
          " q(g({})) = \t{} \n"
          " p(g({})) = \t{} \n"
          " v(g({})) = \t{}".format(i+1, b[i],i+1, qb[i],i+1, pb[i],i+1, vb[i]))



#############################################################
#       RUN ELECTRE TRI TO ASSIGN ALTERNATIVE 'a'
#############################################################


approx = input_bool("Use approximation for cj: yes/no ?")

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


### PRINT RESULTS

print("\nPartial concordance indices: \n")
for i in range(0,h,1):
    print("c(a,b{}) = {}".format(i+1, ab[i][0]))

print("\nComprehensive concordance indices: \n")
for i in range(0,h,1):
    print("C(a,b{}) = {}".format(i+1, ab[i][1]))

print("\nDiscordance indices: \n")
for i in range(0,h,1):
    print("d(a,b{}) = {}".format(i+1, ab[i][2]))

print("\nCredibility indices \n")
for i in range(0,h,1):
    print(" rho(a,b{}) = {} ".format(i+1, ab[i][3]))

print("\nOutranking relations\n")
for i in range(0,h,1):
    if ab[i][4]==True:
        print("aSb{}".format(i+1))
    else:
        print("not(aSb{})".format(i+1))

### assignment with pessimistic procedure
for i in range(h,0,-1):
    if S[i-1] == True:
        print("The pessimistic procedure assigns 'a' to category C{}".format((i+1)))
        break
else:
    print("The pesimistic procedure assigns 'a' to category C1") ## on supppose que a surclasse forcement b0
    # , et par defaut assigne a la moins bonne des cate c0


