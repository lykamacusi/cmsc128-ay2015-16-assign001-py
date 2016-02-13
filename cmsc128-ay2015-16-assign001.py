#Accepts a whole number from zero(0) to 1 million(1000000 - without commas) and prints the number in word form
def	numToWords():
	print("Number to words");


#-------------------------------------------------------------------------------------------------------------
#Accepts a number in word form (from zero to 1 million) and returns it in numerical form
#Input must be in lowercase
def wordsToNum():
	print("Words to number");


#-------------------------------------------------------------------------------------------------------------
#Accepts two arguments: the first argument is the number in word form (from zero to 1 million)
#and the second argument isany of the following: JPY, PHP, USD.
#The function returns the number in words to its numerical form with a prefix of the currency
def wordsToCurency():
	print("Words to currency");


#-------------------------------------------------------------------------------------------------------------
#Accepts three arguments: the first is the number from zero to 1 miliion,
#the second is the delimiter to be used (single character only)
#and third, the number of jumps when the delimiter will appear (from right most going to left most digit)
def numberDelimited():
	print("Number delimited");


#-------------------------------------------------------------------------------------------------------------
#Function for printing the menu
def printMenu():
	choice = 5;	#initialize choice to 5
	
	while(choice != 0):	#while choice is not equal to 0
		print("***********************************");
		print("*                                 *");
		print("*     [ 1 ] Number to words       *");
		print("*     [ 2 ] Words to number       *");
		print("*     [ 3 ] Words to currency     *");
		print("*     [ 4 ] Number delimited      *");
		print("*     [ 0 ] Exit                  *");
		print("*                                 *");
		print("***********************************");
	
		choice = int(input("Enter choice: ")) #asks what the user wants to do

		if choice == 1:
			numToWords();	#calls the number to words function
		elif choice == 2:
			wordsToNum();	#calls the words to number function
		elif choice == 3:
			wordsToCurreny();	#calls the words to currency function
		elif choice == 4:
			numberDelimited();	#calls the number delimited function
		elif choice == 0:
			print("\nProgram Terminated...");
		else:
			print("Invalid input!");
	
printMenu();
