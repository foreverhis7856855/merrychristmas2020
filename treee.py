Python 3.7.5 (default, Nov  7 2019, 10:50:52) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(5):
	for j in range(5):
		print('★', end='')

		
★★★★★★★★★★★★★★★★★★★★★★★★★
>>> for i in range(5):
	for j in range(5):
	    print('*', end='')

	    
*************************
>>> for i in range(5):
	print('*')

	
*
*
*
*
*
>>> for i in range(3):
	for j in range(7):
		print('★')

		
★
★
★
★
★
★
★
★
★
★
★
★
★
★
★
★
★
★
★
★
★
>>> for i in range(3):
	for j in range(7):
		print('★', end='')

		
★★★★★★★★★★★★★★★★★★★★★
>>> for i in range(3):
	for j in range(7):
		print('★', end='')
		print()

		
★
★
★
★
★
★
★
★
★
★
★
★
★
★
★
★
★
★
★
★
★
>>> for i in range(3):
	for j in range(7):
		print('★', end='')
	print()

	
★★★★★★★
★★★★★★★
★★★★★★★
>>> 
