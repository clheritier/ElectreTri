" checking if input type is the one expected"


import numpy as np


#def input_int(message):
#    """converting and checking: str(input) to int>0.  if error: user has to enter an other one"""
#    while True:
#        try:
#            userInput = int(input(message))
#        except ValueError:
#            print("It is not an integer.")
#            continue
#        else:
#            return userInput
            #break

###############################################################

def input_array(message,length): # pb retour valueError pourtant n'accepte pas str
    """converting and checking: str(input) to array of floats.  if error: user has to enter an other one"""

    while True:
        try:
            userInputVec = input(message)
            userInputVec = np.fromstring(userInputVec, dtype=float, sep = ',')
        except ValueError:
            print("error")
        if np.size(userInputVec)!=length:
            print("size of the vector is not correct")
        else:
            #print(userInputVec)
            return userInputVec
            #break


###############################################################

def input_int_positif(message):
    """converting and checking: str(input) to int.  if error: user has to enter an other one"""
    while True:
        try:
            userInput = int(input(message))
            if userInput <= 0:
                    raise ValueError
        except ValueError:
            print("It is not an integer or value is <0.")
            continue
        else:
            return userInput
            #break

###############################################################

def input_lambda(message):
    """converting and checking: str(input) to float in [0.5,1]  if error: user has to enter an other one"""
    while True:
        try:
            userInput = float(input(message))
            if userInput>1 or userInput<0.5:
                    raise ValueError
        except ValueError:
            print("error, value must be in [0.5, 1].")
            continue
        else:
            return userInput
            #break


###############################################################
def input_bool(message):
    while True:
        try:
           return {"yes":True,"no":False}[input(message).lower()]
        except KeyError:
           print("Invalid input, enter yes or no.")


###############################################################
def input_gamma(message):
    """converting and checking: str(input) to float in ]0,1]  if error: user has to enter an other one"""
    while True:
        try:
            userInput = float(input(message))
            if userInput>1 or userInput<=0:
                    raise ValueError
        except ValueError:
            print("error, value must be in ]0, 1].")
            continue
        else:
            return userInput
            #break