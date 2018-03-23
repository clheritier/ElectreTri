
import numpy as np

#from input_checking import*
n=3
p=4


b = np.empty((0,n))
#for i in range(1,p,1):
    #new_row = input_array("enter profile b {}".format((i)), n)
    #b = np.append(b, [new_row],0)
#for i in range(1,p,1):
    #print("\n profile b{} = {} ".format(i, b[i-1]))

#print(b[1])
#print(b[2])
#print(b[0,2])



def input_lambda(message):
    """converting and checking: str(input) to int.  if error: user has to enter an other one"""
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

input_lambda("entrer lambda")
