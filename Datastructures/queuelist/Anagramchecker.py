"""
Desc:Take a range of 0 - 1000 Numbers and find the Prime numbers in that range.
     In a 2D Array the numbers that are Anagram and numbers that are not Anagram.

Created on Thu Jan 02 14:03:09 2020
@author: Moneshs
"""

TEN = 10
A=[]
B=[]
# Function to update the frequency array 
# such that freq[i] stores the 
# frequency of digit i in n 
def updateFreq(n, freq) : 
	'''
    parameters:int
	   n- number to check
	   freq-frequency of a digit
	return:
	   frequency of i 
	'''

	# While there are digits 
	# left to process 
	while (n) : 
		digit = n % TEN 

		# Update the frequency of 
		# the current digit 
		freq[digit] += 1

		# Remove the last digit 
		n //= TEN 

# Function that returns true if a and b 
# are anagarams of each other 
def areAnagrams(a, b): 
	'''
	params:int
	  a,b=no to check is a anagram or not
	return:
	  list:
	     numbers which are anagram
	'''

	# To store the frequencies of 
	# the digits in a and b 
	freqA = [ 0 ] * TEN 
	freqB = [ 0 ] * TEN 

	# Update the frequency of 
	# the digits in a 
	updateFreq(a, freqA) 

	# Update the frequency of 
	# the digits in b 
	updateFreq(b, freqB) 

	# Match the frequencies of 
	# the common digits 
	for i in range(TEN): 

		# If frequency differs for any digit 
		# then the numbers are not 
		# anagrams of each other 
		if (freqA[i] != freqB[i]): 
			return False
			
	A.append(a)
	B.append(b)