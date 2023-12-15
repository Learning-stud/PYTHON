class Vehicle1():
    print("Type 1")


class Vehicle2(Vehicle1):
    print("Type 2")


class Vehicle3(Vehicle2):
    print("Type 3")


cars= Vehicle3()