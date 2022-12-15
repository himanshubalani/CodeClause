import operations as op

print('''
/  __ \         | |    /  __ \ |
| /  \/ ___   __| | ___| /  \/ | __ _ _   _ ___  ___
| |    / _ \ / _` |/ _ \ |   | |/ _` | | | / __|/ _ |
| \__/\ (_) | (_| |  __/ \__/\ | (_| | |_| \__ \  __/
 \____/\___/ \__,_|\___|\____/_|\__,_|\__,_|___/\___|


 _____       _             _       _
/  __ \     | |           | |     | |
| /  \/ __ _| | ___  _   _| | __ _| |_ ___  _ __
| |    / _` | |/ __|| | | | |/ _` | __/ _ \| '__|
| \__/\ (_| | | (__|| |_| | | (_| | || (_) | |
 \____/\__,_|_|\___|\__,_/|_|\__,_|\__\___/|_|
 ''')

print("Choose an operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
print("6.Square root")
print("7.Sine")
print("8.Cosine")
print("9.Tangent")
print("10.Exit")

choice = input("Enter choice(1/2/3/4/5/6/7/8/9):")

def inpnum1():
	return int(input("Enter first number: "))

def inpnum2():
	return int(input("Enter second number: "))

if choice == '1':
	num1 = inpnum1()
	num2 = inpnum2()
	print(num1,"+",num2,"=", op.add(num1,num2))

elif choice == '2':
	num1 = inpnum1()
	num2 = inpnum2()
	print(num1,"-",num2,"=", op.subtract(num1,num2))

elif choice == '3':
	num1 = inpnum1()
	num2 = inpnum2()
	print(num1,"*",num2,"=", op.multiply(num1,num2))

elif choice == '4':
	num1 = inpnum1()
	num2 = inpnum2()
	print(num1,"/",num2,"=", op.divide(num1,num2))

elif choice == '5':
	num1 = inpnum1()
	num2 = inpnum2()
	print(num1,"^",num2,"=", op.power(num1,num2))

elif choice == '6':
	num1 = inpnum1()
	print("Square root of",num1,"=", op.square_root(num1))

elif choice == '7':
	num1 = inpnum1()
	print("Sine of",num1,"=", op.sine(num1))

elif choice == '8':
	num1 = inpnum1()
	print("Cosine of",num1,"=", op.cosine(num1))

elif choice == '9':
	num1 = inpnum1()
	print("Tangent of",num1,"=", op.tangent(num1))

elif choice == '10':
	exit()

else:
	print("Invalid input")