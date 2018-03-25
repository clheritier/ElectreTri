"""Electre III indices modules """

import os
import numpy as np
import math
from input_checking import *

def partial_concordance(a, b, qb, pb):
    """ Computes the partial concordance indices cj(a,b). Parameters to provide are (a, b, qb, pb)
     such that:
        - a: the performance vector of alternative a. a = [g1(a), g2(a), ..., gj(a)]. Type(a) must be <class 'numpy.ndarray'>
        - b: the performance vector of alternative b. b = [g1(b), g2(b), ..., gj(b)]. Type(b) must be <class 'numpy.ndarray'>
        - qb: vector of indifference thresholds associated to b. qb = [q1(g(b)), ..., qj(g(b))]. Type(qb) must be <class 'numpy.ndarray'>
        - pb: vector of preference thresholds associated to b. pb = [p1(g(b)), ..., pj(g(b))]. Type(qb) must be <class 'numpy.ndarray'>
    the function return the vector of partial concordances cj(a,b)"""



    c_ab = np.zeros(np.size(a), float)

    for i in range(0, np.size(a)):
        if a[i] <= (b[i] - pb[i]):
            c_ab[i] = 0
        elif (b[i] - qb[i]) <= a[i]:
            c_ab[i] = 1
        else:
            c_ab[i] = ((a[i] - b[i] + pb[i])/(pb[i] - qb[i]))
    return c_ab



def partial_concordance_approx(a, b, qb, pb):
    """ Computes the partial concordance indices cj(a,b) approximated by a sigmoidal function. (cf Mousseau & Slowinski, 1998)
     Parameters to provide are (a, b, qb, pb)
     such that:
        - a: the performance vector of alternative a. a = [g1(a), g2(a), ..., gj(a)]. Type(a) must be <class 'numpy.ndarray'>
        - b: the performance vector of alternative b. b = [g1(b), g2(b), ..., gj(b)]. Type(b) must be <class 'numpy.ndarray'>
        - qb: vector of indifference thresholds associated to b. qb = [q1(g(b)), ..., qj(g(b))]. Type(qb) must be <class 'numpy.ndarray'>
        - pb: vector of preference thresholds associated to b. pb = [p1(g(b)), ..., pj(g(b))]. Type(qb) must be <class 'numpy.ndarray'>
    the function return the vector of partial concordances cj(a,b) """

    c_ab = np.zeros(np.size(a), float)     # voir avec np.empty

    for i in range(0, np.size(a)):
        e = ((-5.55 /(pb[i] - qb[i])) * (a[i] - b[i] + (0.5*(pb[i] + qb[i]))))
        c_ab[i] = 1/(1 + math.exp(e))
    return c_ab



def comprehensive_concordance(c_ab, w):
    """ Computes the comprehensive concordance index C(a,b) (type 'float')
     Parameters to provide are (c_ab, k)
     such that:
        - cj:  the vector of partial concordances cj(a,b). c_ab = [c1(a,b),..., cj(a,b)]. Type(c_ab) must be <class 'numpy.ndarray'>
        - w: vector of criteria importance coefficient w = [w1, ..., wj]. Type(w) must be <class 'numpy.ndarray'>
    the function return the comprehensive concordance index C(a,b) """

    C_ab = 0
    for i in range(0, np.size(w)):
        C_ab = C_ab + (c_ab[i]*w[i])
    return (C_ab / np.sum(w))

def discordance(a, b, pb, vb):
    """ Computes the discordance index dj(a,b)
     Parameters to provide are (a, b, pb, vb)
     such that:
        - a: the performance vector of alternative a. a = [g1(a), g2(a), ..., gj(a)]. Type(a) must be <class 'numpy.ndarray'>
        - b: the performance vector of alternative b. b = [g1(b), g2(b), ..., gj(b)]. Type(b) must be <class 'numpy.ndarray'>
        - pb: vector of preference thresholds associated to b. pb = [p1(g(b)), ..., pj(g(b))]. Type(qb) must be <class 'numpy.ndarray'>
        - vb: vector of veto thresholds associated to b. vb = [v1(g(b)), ..., vj(g(b))]. Type(vb) must be <class 'numpy.ndarray'>
    the function return the vector of individual discordance indices dj(a,b) """

    d_ab = np.zeros(np.size(a), float)

    for i in range(0, np.size(a)):
        if a[i] <= (b[i] - vb[i]):
            d_ab[i] = 1
        elif (b[i] - pb[i]) <= a[i]:
            d_ab[i] = 0
        else:
            d_ab[i] = ((a[i] - b[i] + pb[i])/(pb[i] - vb[i]))
    return d_ab

def credibility(C_ab, d_ab):
    """ computes the credibility index rho(a,b) (type 'float'
     Parameters to provide are (c, dj)
     - c: comprehensive concordance C(a,b), type 'float"
     -dj: vector of individual discordance indices, dj =[d1(a,b), ..., dj(a,b)]
    """
    ND = 1
    for i in range(0, np.size(d_ab)):
        if d_ab[i] > C_ab:
            ND = ND*(1 - d_ab[i])/(1-C_ab)
    rho= C_ab*ND
    return(rho)


def electre_3(a,b,qb,pb,vb,w,cut_level):
    """ compute the outranking relation S(a,b)? btw alternatives a and b. return aSb or not(aSb)"""
    approx = input_bool("Use approximation for cj: yes/no ?")
    if approx == False:
        cj = partial_concordance(a, b, qb, pb)
    else:
        cj = partial_concordance_approx(a, b, qb, pb)

    C = comprehensive_concordance(cj, w)
    dj = discordance(a,b, pb, vb)
    rho = credibility(C,dj)

    S=False
    if rho>cut_level:
        S= True

    return list([cj,C,dj,rho,S])


# test

if __name__ == "__main__":

    a = np.array([-22, 88, -52, -30, 2, 4, 2, 4])
    b = np.array([-7, 96, -34, -47, 3, 3, 3, 3])
    qb = np.array([5, 8, 4, 3, 0, 0, 0, 0])
    pb = np.array([10, 10, 7, 6, 1, 1, 1, 1])
    vb = np.array([80, 40, 70, 200, 3, 2, 2, 3])
    k = np.array([11.28, 41.7, 14.9, 5.77, 7.84, 4.06, 7.86, 17])

    print("Given the alternatives a and b, defined by their performance on each criterion j in F: \n g(a) = {} \n g(b) = {}\n".format(a,b))
    print("Alternative b is defined with the following thresholds: \n q(g(b)) = {} \n p(g(b)) = {} \n v(g(b)) = {} \n".format(qb,pb,vb))

    print("Importance coefficient are defined for the {} criteria, such as \n w = {} \n".format(np.size(k), k))

    print(" *** BUILDING THE FUZZY OUTRANKING RELATION (a,b) *** \n")

    cj = partial_concordance(a,b,qb,pb)
    cj_approx = partial_concordance_approx(a,b,qb,pb)
    c = comprehensive_concordance(cj,k)
    dj = discordance(a,b,pb,vb)
    rho = credibility(c,dj)

    print("The partial concordance cj(a,b) is: \n c(a,b) = {} \n"
          "(using the approximation, we have: c(a,b)_approx = {}) \n \n"
          "The comprehensive concordance is: \n C(a,b) = {} \n \n"
          "The discordance index dj(a,b) is: \n d(a,b) = {}\n \n"
          "The credibility of the assertion 'a is at last as good as b' is: \n rho(a,b) = {}".format(cj,cj_approx,c,dj,rho))

    os.system("pause")

