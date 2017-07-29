x = input("input salary ")
salary = int(x)
grade = int(input("input grade "))
dept = input("input dept it or hr ")
pos = input("input position cto ")
if salary <= 15000:
	out = salary
	print(out)

else:	
	if dept == "hr":
		if grade <= 10:
			out = salary -(salary - 15000)*0.09
			print (out)

		if grade in range (11, 20):
			out = salary -(salary - 15000)*0.17
			print (out)
		if pos == "cto":
			out = salary +(salary *0.02)
			print (out)
	if dept == "it":
		if grade <= 10:
			out = salary -(salary - 15000)*0.09
			print (out)
		if grade in range (11, 20):
			out = salary -(salary - 15000)*0.15
			print (out)	
		if pos == "cto":
			out = salary +(salary *0.05)	
			print ("with bonus", out)


			


