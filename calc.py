def add(x,y):
	return x+y
def sub(x,y):
	return x-y
def mult(x,y):
	return x*y
def div(x,y):
	return x/y

print("select the choice for calculation")
print("1. Addition")
print("2. Substraction")
print("3. Muliplication")
print("4. Divison")

n = int(raw_input())
num1 = int(raw_input("Enter the first number "))
num2 = int(raw_input("Enter the second number "))

if n==1:
	print add(num1,num2)
elif n==2:
	print sub(num1,num2)
elif n==3:
	print mult(num1,num2)
elif n==4:
	print div(num1,num2)
else:
	print("Invalid selection")
	 