# def main():
#     number = int(input("Enter a number: "))  # User se ek number input lo
#     result = squared(number)  # Squared function ko call karke result ko store karo
#     print("The square of", number, "is", result)  # Result ko print karo

# def squared(multi):
#     return multi * multi  # Diye gaye number ka square return karo

# main()  # main() function ko call karo

# The main function takes a number as input, calls the squared function to calculate the square of the number, and then prints the result.


def main():

    number = int(input("Enter any number: "))
    result = squared(number)
    print("The Square of", number , "is", result )

def squared(multi):

    '''
Also can be written in this type its and    python in build function {return pow(multi, 2)}
    '''
    return  multi * multi

main()