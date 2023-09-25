
def main():
	print()
	print('Would you like to:')
	print('   a) Find the molar mass of a compound')
	print('   b) Find the number of moles in a compound')
	print('   c) Find the mass of a compound')
	choice = input("Please select 'a', 'b', or 'c' : ")
	choice = choice.lower()
	wrongImput = True
	if (choice == 'a') or (choice == 'b') or (choice == 'c') or (choice == "'a'") or (choice == "'b'") or (choice == "'c'"):
		wrongImput = False
	while (wrongImput==True): #makes sure valid input
		choice = input("Please select 'a', 'b', or 'c' : ")
		choice = choice.lower()
		if (choice == 'a') or (choice == 'b') or (choice == 'c') or (choice == "'a'") or (choice == "'b'") or (choice == "'c'"):
			wrongImput = False
	if (choice == 'a') or (choice =="'a'"):
		decision = 'a'
	if (choice == 'b') or (choice =="'b'"):
		decision = 'b'
	if (choice == 'c') or (choice =="'c'"):
		decision = 'c'
	#The following block of code is for decision a
	if decision == 'a':
		print()
		molarMass = find_molar_mass()
		print()
		print('The molar mass of the compound is',molarMass,'g/mol')

	#The following block of code is for decision b
	if decision == 'b':
		print()
		molarMass = find_molar_mass()
		print()
		knownMass = input('Enter the known mass of the sample in grams: ')
		passInt = False
		while passInt ==False:
			try:
				knownMass = float(knownMass)
				passInt = True
				if (knownMass <= 0):
					passInt = False
					knownMass = input('Please input a mass greater than 0: ')
			except:
				knownMass = input('Please input a number: ')
		moles = find_moles(molarMass, knownMass)
		print(f'In the {knownMass} g sample, there are {moles:.5f} moles')

	#The following block of code is for decision c
	if decision == 'c':
		print()
		molarMass = find_molar_mass()
		print()
		knownMoles = input('Enter the known number of moles in the sample: ')
		passInt = False
		while passInt ==False:
			try:
				knownMoles = float(knownMoles)
				passInt = True
				if (knownMoles <= 0):
					passInt = False
					knownMoles = input('Please input a mass greater than 0: ')
			except:
				knownMoles = input('Please input a number: ')
		grams = find_grams(molarMass, knownMoles)
		print('The',knownMoles,'mole sample has a mass of',grams,'g')

def find_molar_mass():
		elements = ['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe',
		'Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te',
		'I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au',
		'Hg','Tl','Pb','Bi','Po','At','Rn','Fr','Ra','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','Rf','Db',
		'Sg','Bh','Hs','Mt','Ds','Rg','Cn','Nh','Fl','Mc','Lv','Ts','Og']
		done = False
		compound = []
		while done == False: #This while loop gets all the information from the user regarding their compound
			elem = input("Please input an element's chemical symbol: ")
			while (elem not in elements): #This while loop confirms a valid chemical symbol was inputted
				print("please input an element's chemical symbol, pay attention to capitalization (gold = Au)")
				elem = input("element: ")
			elemOccurance = input('Please input the amount of that element present in the compound: ')
			passInt = False
			while passInt == False: #This while loop confirms that a valid integer greater than 0 was inputted
				try:
					elemOccurance = int(elemOccurance)
					passInt = True
					if (elemOccurance <= 0):
						passInt = False
						elemOccurance = input('Please input an integer greater than 0: ')
				except:
					elemOccurance = input('Please input an integer: ')
			for num in range(1,elemOccurance+1): #This for loop adds the elements imputted in the proper quantity to the compound list
				compound = compound + [elem]
			finish = input('Are there more elements? ') #This segment asks if the user is done and confirms a proper input
			finish = finish.lower()
			options = ['yes','no','y','n','done']
			while finish not in options: #This while loop confirms a valid input
				print('Please input "yes" or "no"')
				finish = input('Are there more elements? ')
				finish = finish.lower()
			print()
			if finish == 'no': #these three if statments indicate the user is done inputting elements and exits the while loop
				done = True
			if finish == 'n':
				done = True
			if finish == 'done':
				done = True
		dictionary = {'H':1.01,'He':4.00,'Li':6.94,'Be':9.01,'B':10.81,'C':12.01,'N':14.01,'O':16.00,'F':19.00,'Ne':20.18,'Na':22.99,
		'Mg':24.31,'Al':26.98,'Si':28.09,'P':30.97,'S':32.06,'Cl':35.45,'Ar':39.95,'K':39.10,'Ca':40.08,'Sc':44.96,'Ti':47.88,'V':50.94,
		'Cr':51.99,'Mn':54.94,'Fe':55.85,'Co':58.93,'Ni':58.69,'Cu':63.55,'Zn':65.38,'Ga':69.72,'Ge':72.63,'As':74.92,'Se':78.97,
		'Br':79.90,'Kr':83.80,'Rb':85.47,'Sr':87.62,'Y':88.91,'Zr':91.22,'Nb':92.91,'Mo':95.95,'Tc':98.91,'Ru':101.07,'Rh':102.91,
		'Pd':106.42,'Ag':107.87,'Cd':112.41,'In':114.82,'Sn':118.71,'Sb':121.76,'Te':127.6,'I':126.90,'Xe':131.29,'Cs':132.91,'Ba':137.33,
		'La':138.91,'Ce':140.12,'Pr':140.91,'Nd':144.24,'Pm':144.91,'Sm':150.36,'Eu':151.96,'Gd':157.25,'Tb':158.93,'Dy':162.50,'Ho':164.93,
		'Er':167.26,'Tm':168.93,'Yb':173.06,'Lu':174.97,'Hf':178.49,'Ta':180.95,'W':183.85,'Re':186.21,'Os':160.23,'Ir':192.22,'Pt':195.08,
		'Au':196.97,'Hg':200.59,'Tl':204.38,'Pb':207.20,'Bi':208.98,'Po':208.98,'At':209.98,'Rn':222.02,'Fr':223.02,'Ra':226.03,'Ac':227.03,
		'Th':232.04,'Pa':231.04,'U':238.03,'Np':237.05,'Pu':244.06,'Am':243.06,'Cm':247.07,'Bk':247.07,'Cf':251.08,'Es':254,'Fm':257.10,
		'Md':258.10,'No':259.10,'Lr':262,'Rf':261,'Db':262,'Sg':266,'Bh':264,'Hs':269,'Mt':278,'Ds':281,'Rg':280,'Cn':285,'Nh':286,
		'Fl':289,'Mc':289,'Lv':293,'Ts':294,'Og':294}
		molarMass = 0
		for elem in compound: #this for loop adds the mass of each element in the list together
			molarMass = molarMass + dictionary[elem]
		return molarMass

def find_moles(molarMass,knownMass):
	moles = (knownMass)/(molarMass)
	return moles

def find_grams(molarMass,knownMoles):
	grams = (knownMoles)*(molarMass)
	return grams

if __name__ == '__main__':
	main()
