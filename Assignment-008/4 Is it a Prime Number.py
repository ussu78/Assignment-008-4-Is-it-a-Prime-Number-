Task : 
  Write a program that takes a number from the user and prints the result to check if it is a prime number.
  
  num = int(input("Enter a number to check if it is a prime number:"))
if num > 1:

    for i in range(2, int(num / 2) + 1):

        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")
