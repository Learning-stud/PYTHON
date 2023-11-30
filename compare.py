# User se x ki value input lo
x = input("Enter the value of x: ")

# User se y ki value input liya
y = input("Enter the value of y: ")

# Check kiya ki x aur y mein sirf numbers hain ya nahi
if x.isdigit() and y.isdigit():
    # Agar numbers hain, toh unko integer mein convert kiya
    x = int(x)
    y = int(y)

    # Check kiya ki x chhota hai y se ya nahi
    if x < y:
        print("y is greater")
    # Agar x aur y barabar hain
    elif x == y:
        print("x is equal to y")
    # Agar x bada hai y se
    else:
        print("x is greater")
else:
    # Agar koi bhi number nahi hai toh "No number entered" print kiya
    print("No number entered")
