"""
Authors: Jesse Contreras, Damini Gopal
Serial Numbers: 22, 33
Spring 2020 - CS 1342 - 251
Homework Number 4
Due Date : April, 6th 2020
"""

num1 = 0     #int input that tells the exclusive lower bound of the range
             #cannot be negative, more than, or equal to num2

num2 = 0     #int input that tells the exclusive upper bound of the range 
             #cannot be negative, less than, or equal to num1

evens = []   #list of even ints in the range(x)
             #range(x) = num1 < x < num2

odds = []    #list of odd ints x in the range(x)
             #range(x) = num1 < x < num2

primes = []  #list of prime ints x in the range(x)
             #range(x) = num1 < x < num2

print("This program is written by Jesse Contreras and Damini Gopal\n")
print("The function of this program is, given 2 positive numbers,")
print("the program will display the following\n\n")
print("\t1. All even numbers between firstNum and secondNum.")
print("\t2. All odd numbers between firstNum and secondNum.")
print("\t3. Sum of all even numbers between firstNum and secondNum.")
print("\t4. Sum of all odd numbers between firstNum and secondNum.")
print("\t5. All prime numbers between firstNum and secondNum.")
print("\t6. The numbers and their squares between firstNum and")
print("\t   secondNum exclusive.\n\n")

num1 = int(input("Enter The First Number : "))
num2 = int(input("Enter The Second Number : "))

if (num1 >= 0 and num2 >= 0): #check if numbers are positive
    if(num1 < num2): #check if num1 < num2
        
        print("\n\nYou entered :",num1,"and",num2,"\n\n")
        for i in range(num1+1, num2): #exclusive range

            #Code for finding if i is even or odd
            if (i%2==0):evens.append(i) #if divisible by 2 add to evens[]
            else: odds.append(i) #if not add to odds[]

            #Code for getting primes[]
            primes.append(i) #append current i to primes[]
            if(i==1): primes.remove(1) #1 is not prime
            for j in range(2,i//2+1):
                if(i%j==0):
                    primes.remove(i) #remove i from primes[] if divisible
                    break

        print("1. All Even Numbers :", ','.join(list(map(str, evens))))
        print("2. All Odd Numbers :", ','.join(list(map(str, odds))))
        print("3. Sum Of All Even Numbers :",sum(evens))
        print("4. Sum of All Odd Numbers :",sum(odds))
        print("5. AllPrimeNumbers :", ','.join(list(map(str, primes))))
        print("6. Number    Square")
        for x in range(num1+1,num2): print("     "+ str(x).ljust(9) + str(x*x))
        
    else: print("\n\nError : First Number Must Be < Second Number.")
else: print("\n\nError - Invalid Number : Numbers must be Positive.")

#Singature Line
print("\n\nProgram is implement by Jesse Contreras and Damini Gopal\n3-4-20")
