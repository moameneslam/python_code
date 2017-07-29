x = input ("enter a number: ")
x1 = int(x)
if x1 > 100:
	print ("A")
	if x1 > 500:
		print ("1")
	else:
		print ("2")	
else:
	print ("B")	
	if x1 < 50:
		print("4")
	else:
		print("3")	