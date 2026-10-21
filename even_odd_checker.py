# Even or Odd number checker
def main():
    number = int(input("Enter a number: "))

    # calling even number checker function
    if even_number(number):
        print("Even number")
    else:
        print("Odd number")

# defining the even number checker function
def even_number(n):
    if n % 2 == 0:
        return True
    else:
        return False


# calling the main function
main()