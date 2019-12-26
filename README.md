# BridgeLabz

Algorithm Programs

1.Write static functions to return all permutations of a String using iterative method and Recursion method. Check if the arrays returned by two string functions are equal. 

2.Binary Search the Word from Word List
Desc -> Read in a list of words from File. Then prompt the user to enter a word to search the list. The program reports if the search word is found in the list.
I/P -> read in the list words comma separated from a File and then enter the word to be searched
Logic -> Use Arrays to sort the word list and then do the binary search
O/P -> Print the result if the word is found or not

3.Insertion Sort 
Desc -> Reads in strings and prints them in sorted order using insertion sort.
I/P -> read in the list words
Logic -> Use Insertion Sort to sort the words in the String array
O/P -> Print the Sorted List

4.Bubble Sort 
Desc -> Reads in integers prints them in sorted order using Bubble Sort
I/P -> read in the list ints
O/P -> Print the Sorted List 

5.Merge Sort  - Write a program to do Merge Sort of list of Strings. 
Logic -> To Merge Sort an array, we divide it into two halves, sort the two halves independently, and then merge the results to sort the full array. To sort a[lo, hi), we use the following recursive strategy:
Base case: If the subarray length is 0 or 1, it is already sorted.
Reduction step: Otherwise, compute mid = lo + (hi - lo) / 2, recursively sort the two subarrays a[lo, mid) and a[mid, hi), and merge them to produce a sorted result.

6.An Anagram Detection Example
Desc -> One string is an anagram of another if the second is simply a rearrangement of the first. For example, 'heart' and 'earth' are anagrams...
I/P -> Take 2 Strings as Input such abcd and dcba and Check for Anagrams
O/P -> The Two Strings are Anagram or not....

7.Take a range of 0 - 1000 Numbers and find the Prime numbers in that range. 

8.Extend the above program to find the prime numbers that are Anagram and Palindrome 

9.Question to find your number
Desc -> takes a command-line argument N, asks you to think of a number between 0 and N-1, where N = 2^n, and always guesses the answer with n questions.
I/P -> the Number N and then recursively ask true/false if the number is between a high and low value
Logic -> Use Binary Search to find the number
O/P -> Print the intermediary number and the final answer

10.Customize Message Demonstration using String Function and RegEx
Desc -> Read in the following message: Hello <<name>>, We have your full name as <<full name>> in our system. your contact number is 91-xxxxxxxxxx. Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016. Use Regex to replace name, full name, Mobile#, and Date with proper value.
I/P -> read in the Message
Logic -> Use Regex to do the following
Replace <<name>> by first name of the user ( assume you are the user)
replace <<full name>> by user full name.
replace any occurance of mobile number that should be in format 91-xxxxxxxxxx by your contact number.
replace any date in the format XX/XX/XXXX by current date.
O/P -> Print the Modified Message.



