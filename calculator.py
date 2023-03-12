def add(a, b):
      return a + b


def subtract(a, b):
  return a - b


def multiply(a, b):
  return a * b


def divide(a, b):
  return a / b


print('what do  you want to do')
print('1=addition')
print('2=subtraaction')
print('3=multiplication')
print('4=division')

while True:
  choice = input('enter choice(1/2/3/4)')
  if choice in ('1', '2', '3', '4'):
    num1 = float(input('enter first number'))
    num2 = float(input('enter second number'))

    if choice == '1':
      print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
      print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
      print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
      print(num1, "/", num2, "=", divide(num1, num2))

    next_calculation = input('want to do another calculation(yes/no)')
  if next_calculation == ('no'):
     break
  else:
    print('invalid input')
