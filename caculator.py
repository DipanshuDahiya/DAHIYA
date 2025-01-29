a=("My calculator")
print(a.center (50))
a = int(input("Enter first number: "))
o = input("enter operater: ")
b = int(input("Enter second number: "))
if (o == '+'):
  print(a + b)
elif (o == '-'):
  print(a - b)
elif (o == '*'):
  print(a * b)
elif (o == '/'):
  print(a / b)
else:
  print("invalid operater")
print("Thank you for using my calculator")
