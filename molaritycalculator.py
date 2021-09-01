calc = input("What would you like to calculate? Enter conc or mass or vol : ")
if calc == "conc":
	volconc = input("Enter volume in mL: ")
	mwconc = input("Enter molecular weight: ")
	massconc = input("Enter mass in grams: ")
	finalconc = (float(massconc) / ( float(volconc) * float (mwconc) )) * 1000
	finalmM = float(finalconc) * 1000
	print(str(finalconc) + " M")
	print(str(finalmM) + " mM")

if calc == "mass":
	mconc = input("Enter concentration in mM: ")
	mfw = input("Enter molecular weight: ")
	mvol = input("Enter volume in mL: ")
	mcalc = float(mconc) * float(mvol) * float(mfw)/ 1000000
	mcalcmg = float(mcalc) * 1000
	print(str(mcalc) + " g")
	print(str(mcalcmg) + " mg")

if calc == "vol":
	volmass = input("Enter mass in g: ")
	volfw = input("Enter molecular weight: ")
	volconc = input("Enter concentration in mM: ")
	volcalcmL = float(volmass) / ( float(volfw) * float(volconc) ) * 1000000
	volcalcL = float(volcalcmL) / 1000
	print(str(volcalcmL) + " mL")
	print(str(volcalcL) + " L")
