def calculate_average(numbers):
   sum=0
   for i in numbers:
      sum=sum+i
   return sum / len(numbers)



numbers_list = [10, 20, 30, 40, 50]
average = calculate_average(numbers_list)
print(f"The average is: {average}")

