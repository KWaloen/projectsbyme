forc = input("To which temperature do you want to convert to? F or C: ")

if forc == "C":
	startF = input("Enter temperature in F: ")
	calcF = (float(startF) - 32) * 5/9
	print(str(calcF) + " degrees Celcius")

if forc == "F":
	startC = input("Enter temperature in C: ")
	calcC = (float(startC) * 9/5) + 32
	print(str(calcC) + " degrees Fahrenheit")
