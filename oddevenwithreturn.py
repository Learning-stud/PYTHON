def main():
    even = int(input(" Enter the value => "))
    if is_even(even):
        print("even")
    else:
        print("odd")

def is_even(value):
    if value % 2 == 0:
        return True
    else:
        return False            
    

    # return True if value % 2 == 0 else  False

main()    

