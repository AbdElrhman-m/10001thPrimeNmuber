# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# superBido ;)

What is the 10 001st prime number?
def is_prime(num):
	'''checking if the number is prime or not '''

	check_list = range(2,num)
	if num == 1:
		return False
	if num == 2 or num == 3 or num == 5:
		return True
	if num % 2 == 0 or num % 3 ==0 or num %5 ==0:
		return False
	for n in check_list:
		if num % n == 0:
			return False
	return True

def prime_number(prime_number_find):
	''' print the required number by according to its arange  '''

	prime_number_find = prime_number_find - 1
	x = 1 #starting number 
	list_of_primes = [] 

	while len(list_of_primes) < prime_number_find:
		if is_prime(x) == True :
			list_of_primes.append(x)
		x += 2
	return list_of_primes[len(list_of_primes)-1]

print prime_number(6)
#>>> 13
print prime_number(10001)