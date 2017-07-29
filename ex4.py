Str1 = "QA Consulting"
Str2 = "Office for national statistics"
vowels = "AaOoUuYyIiEe"
for x in Str1:
	for y in vowels:
		if x==y:
			print(x)
			break
		break	
print ("_______________________________________________________")
flag =0
for w in Str2:
	for b in vowels:

		if w==b:
			flag =1
		else:
			pass
	if flag == 0:
		print(w)
	flag =0			

print ("_______________________________________________________")					
		
for i in Str2:
	
	if i not in vowels:
		print (i)			
					
