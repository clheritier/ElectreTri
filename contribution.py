

import itertools

'''
Given a vector vec of numerical values and two parameters lambda_ and beta_ corresponding to numerical values too,
the code computes a collection containing all set of ids s of minimal size
for which the sum of values of vec[id] for all id in s is greater than lambda_ * beta_
The execution stops when after the evaluation of all the sets of size j in [1,len(vec)[
the collection of results is not empty.

Usage : set the values of vec (the code is generic so vec can be of any size)
set the values of lambda_ and beta_

author: sebastien.harispe@mines-ales.fr
'''

lambda_ = 60
beta_ = 0.5

threshold = lambda_ * beta_

vec = [2,3,6,7,4,2,1,9]

print("Computing best subsets")
print("lambda: ",lambda_)
print("beta: ",beta_)
print("threshold: ",threshold)
print("vector", vec)

solutions = []

set_id = set()
for i in range(0,len(vec)):
	set_id.add(i)

print("set of ids: ",set_id)

i = 0
while i< len(vec) and len(solutions) == 0:
	print("Evaluating subsets of size: ",(i+1))
	sets_of_ids_size_i = map(set, itertools.combinations(set_id, i+1))
	print("number of sets: ",len(sets_of_ids_size_i))
	print("searching...")
	for s in sets_of_ids_size_i:
		sum_ = 0
		for j in s:
			sum_ += vec[j]

		if sum_ > threshold:
			print(s," : ", sum_)
			solutions.append((s,sum_))
	i+=1

print("Number of solutions: ",len(solutions))
