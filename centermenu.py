#build menu

title= 'menu'.upper()
rupess=input("Total Items => ")
print(title.center(40, "="))
print("Coffee".ljust(26, "-") + "150rs".rjust(4))
print("Tea".ljust(26, "-") + "100rs".rjust(4))
print("Moccha".ljust(26, "-") + "250rs".rjust(4))
print("Capercino".ljust(26, "-") + "350rs".rjust(4))
print("Red Wine".ljust(26, "-") + "2500rs".rjust(4))
print("Total".ljust(26, "-") + "Rs{rupess}".rjust(4))

# ===============================================================


# title = 'menu'.upper()
# menu_items = {
#     "Coffee": 150,
#     "Tea": 100,
#     "Moccha": 250,
#     "Capercino": 350,
#     "Red Wine": 2500
# }

# print(title.center(40, "="))

# # Display menu items
# for item, price in menu_items.items():
#     print(f"{item.ljust(26, '-')} {price}rs".rjust(4))

# # Initialize total
# total = 0

# # Allow the user to select items
# while True:
#     user_input = input("Enter item (or 'done' to finish): ")

#     if user_input.lower() == 'done':
#         break

#     if user_input in menu_items:
#         total += menu_items[user_input]
#         print(f"{user_input} added to the order.")

# # Display the total
# print(f"Total: Rs {total}")


# title = 'menu'.upper()
# menu_items = {
#     "Coffee": 150,
#     "Tea": 100,
#     "Moccha": 250,
#     "Capercino": 350,
#     "Red Wine": 2500
# }

# print(title.center(40, "="))

# # Display menu items
# for item, price in menu_items.items():
#     print(f"{item.ljust(26, '-')} {price}rs".rjust(4))

# # Initialize total
# total = 0

# # Allow the user to select items
# while True:
#     user_input = input("Enter item (or 'done' to finish): ")

#     if user_input.lower() == 'done':
#         break

#     if user_input in menu_items:
#         total += menu_items[user_input]
#         print(f"{user_input} added to the order.")
#     else:
#         print("Invalid item. Please choose a valid item from the menu.")

# # Display the total
# print(f"Total: Rs {total}")
