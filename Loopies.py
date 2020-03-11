"""
Authors: Jesse Contreras, Damini Gopal
Serial Numbers: 22, 33
Spring 2020 - CS 1342 - 251
Homework Number 4
Due Date : March, 30th 2020
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

ints = []    #list of the ints x in the range(x)
             #range(x) = num1 < x < num2


def list_to_string(my_list):
    my_string = ""
    for n in my_list:
        if (n == my_list[len(my_list)-1]): my_string += str(n)
        else: my_string += str(n)+ ","
    return my_string
    
print("""This program is written by Jesse Contreras and Damini Gopal

The function of this program is, given 2 positive numbers,
the program will display the following


\t1. All even numbers between firstNum and secondNum.
\t2. All odd numbers between firstNum and secondNum.
\t3. Sum of all even numbers between firstNum and secondNum.
\t4. Sum of all odd numbers between firstNum and secondNum.
\t5. All prime numbers between firstNum and secondNum.
\t6. The numbers and their squares between firstNum and
\t   secondNum exclusive.\n\n""")


num1 = int(input("Enter The First Number : "))
num2 = int(input("Enter The Second Number : "))


if (num1 >= 0 and num2 >= 0):
    if(num1 < num2):
        
        print("\n\nYou entered :",num1,"and",num2,"\n\n")
        
        for i in range(num1+1, num2):

            ints.append(i)
            primes.append(i)

            if (i%2==0):evens.append(i)
            else: odds.append(i)
            
            for j in range(2,i):
                if(i%j==0):
                    primes.remove(i)
                    break
                
        print("1. All Even Numbers :",list_to_string(evens))
        print("2. All Odd Numbers :",list_to_string(odds))
        print("3. Sum Of All Even Numbers :",sum(evens))
        print("4. Sum of All Odd Numbers :",sum(odds))
        print("5. AllPrimeNumbers :", list_to_string(primes))
        print("6. Number    Square")
        for x in ints: print("     "+ str(x).ljust(9) + str(x*x))
        
    else:
        print("\n\nError : First Number Must Be < Second Number.")
else:
    print("\n\nError - Invalid Number : Numbers must be Positive.")
