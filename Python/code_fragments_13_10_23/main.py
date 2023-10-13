""" code fragment that will check if the integer stored in variable 'x' is an 'even' integer or an 'odd' integer """

# this function will check if the argument is divisible by 2 or not. If True, it will return "Even" and if False, it will return "Odd".
def is_divisible_by_2(x):
  if (x % 2 == 0):
    return "Even"
  else:
    return "Odd"
  
# test case 1 (let the variable x is assigned with the value 8)
x = 8
print(is_divisible_by_2(x))

# test case 2 (let the variable x is assigned with the value 5)
x = 5
print(is_divisible_by_2(x))


""" code fragment that will check if the value stored in a variable x is divisible by 2 or 7 """

# this function will check if the argument is divisible by 2 or 7, if so, it will return "Divisible", otherwise, it will return "Not divisible"
def is_divisible_by_2_or_7(x):
  if (x % 2 == 0) or (x % 7 == 0):
    return "Divisible"
  else:
    return "Not divisible"

# test case 1 (let the variable x is assigned with the value 5)
x = 5
print(is_divisible_by_2_or_7(x))

# test case 2 (let the variable x is assigned with the value 4)
x = 4
print(is_divisible_by_2_or_7(x))

# test case 3 (let the variable x is assigned with the value 21)
x = 21
print(is_divisible_by_2_or_7(x))

# test case 4 (let the variable x is assigned with the value 28)
x = 28
print(is_divisible_by_2_or_7(x))