# def main():
#     number = int(input("Enter a number: "))  # User se ek number input lo
#     result = squared(number)  # Squared function ko call karke result ko store karo
#     print("The square of", number, "is", result)  # Result ko print karo

# def squared(multi):
#     return multi * multi  # Diye gaye number ka square return karo

# main()  # main() function ko call karo



def main():
    number = int(input("Enter any number: "))
    result = squared(number)
    print("The Square of", number , "is", result )

def squared(multi):
    return  multi * multi

main()