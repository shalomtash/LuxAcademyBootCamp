# Program to check if a number isprime or not

numbers = int(input("Enter a number: "))

# prime numbers are greater than 1


if numbers > 1:
    # check for factors
    for i in range(2, numbers):
        if (numbers % i) == 0:
            print(numbers, "is not a prime number")
            print(i, "times", numbers // i, "is", numbers)
            break
    else:
        print(numbers, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(numbers, "is not a prime number")
