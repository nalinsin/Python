print('Welcome to Online Calculator')

def operator():
	opstr='''PFB the list of operators:
	'+' for addition,
	'-' for subtraction,
	'*' for multiplication,
	'/' for division,
	'**' for power raised to'''
	print(opstr)

def calculator():
	try:
	
		num1=int(input("Enter first number: "))
		num2=int(input("Enter second number: "))
		
		operator()
		
		oper=input("enter operator: ")
		print(num1,oper,num2)
		
		if oper=='+':
			print('Adding...')
			result=num1+num2
		elif oper=='-':
			print('Subtracting...')
			result=num1-num2
		elif oper=='*':
			print('Multiplying...')
			result=num1*num2
		elif oper=='/':
			print('Dividing...')
			result=num1/num2
		elif oper=='**':
			print('calculating power...')
			result=num1**num2

		print('Result is: '+str(result))
	
	except ZeroDivisionError:
		print('ZeroDivision error occurred, please verify the inputs given')
		calculator()
	except:
		print('Error occurred, please verify the inputs given')
		calculator()



def again():
	print('Would you like to calculate again, (Y/N) ?')
	res1=input()
	if res1.upper()=='Y':
		calculator()
	elif res1.upper()=='N':
		print('Calculation is complete. See you again!')
	else: 
		print('Invalid input')
		again()

			
calculator()
again()	

