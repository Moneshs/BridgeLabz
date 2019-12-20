# BridgeLabz

Basic Core Programs

1.User Input and Replace String Template “Hello <<UserName>>, How are you?” 
   I/P -> Take User Name as Input. Ensure UserName has min 3 char
   Logic -> Replace <<UserName>> with the proper name
   O/P -> Print the String with User Name 

2.Flip Coin and print percentage of Heads and Tails
   I/P -> The number of times to Flip Coin. Ensure it is positive integer.
   Logic -> Use Random Function to get value between 0 and 1. If < 0.5 then tails or heads
   O/P -> Percentage of Head vs Tails

3.Leap Year
   I/P -> Year, ensure it is a 4 digit number.
   Logic -> Determine if it is a Leap Year.
   O/P -> Print the year is a Leap Year or not.

4.Power of 2 
   Desc -> This program takes a command-line argument N and prints a table of the powers of 2 that are less than or equal to 2^N.
   I/P -> The Power Value N. Only works if 0 <= N < 31 since 2^31 overflows an int
   Logic -> repeat until i equals N.
   O/P -> Print the year is a Leap Year or not.

5.Harmonic Number 
   Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N (http://users.encs.concordia.ca/~chvatal/notes/harmonic.html).
   I/P -> The Harmonic Value N. Ensure N != 0
   Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
   O/P -> Print the Nth Harmonic Value.

6.Factors
  Desc -> Computes the prime factorization of N using brute force.
  I/P -> Number to find the prime factors 
  Logic -> Traverse till i*i <= N instead of i <= N for efficiency.
  O/P -> Print the prime factors of number N.

