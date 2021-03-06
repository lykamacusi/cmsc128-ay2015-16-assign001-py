#Accepts a whole number from zero(0) to 1 million(1000000 - without commas) and prints the number in word form
def	numToWords(num):
	ones = ['','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
	teens = ['','eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'];
	tens = ['', 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'];
	others = ['', 'thousand', 'million'];
	words = [];	#empty list for storing the string conversion
	
	if num == 0:
		words.append('zero');
	else:
		number = str(num);	#converts int to string
		numberlen = len(number);	#gets the length of the number
		grp = int((numberlen+2)/3);	#how many groups of threes are there(e.g. 1234 -> grp = 2)
									#it's like separating the number with comma(s)(e.g. 1,234)
		number = number.zfill(grp*3);	#pads number on the left with zeros to fill the width(e.g. 001234)
		
		for i in range(grp):	#loops for grp times and increments by 1
			hund = int(number[i*3]);
			ten = int(number[(i*3)+1]);
			o = int(number[(i*3)+2]);
			grp = int(grp-1);
			
			if hund >= 1:
				words.append(ones[hund]);
				words.append('hundred');
			#end of if statement
			
			if ten > 1:
				words.append(tens[ten]);
				if o >= 1:
					words.append(ones[o]);
			elif ten == 1:
				if o >= 1:	#for cases like eleven, twelve, thirteen and so on
					words.append(teens[o]);
				else:	#for cases like twenty, thirty, fourty and so on
					words.append(tens[ten]);
			else:
				if o >= 1:
					words.append(ones[o]);
			#end of else statement
			
			if (grp >= 1) and ((hund+ten+o) > 0):	#checks if the number is in the thousands or millions
				words.append(others[grp]);
			#end of if statement
		#end of for loop
	#end of else statement
	
	print(' '.join(words));	#prints a string in which the elements of the list has been joined by a space
#End of numToWords function


#-------------------------------------------------------------------------------------------------------------
#Accepts a number in word form (from zero to 1 million) and returns it in numerical form
#Input must be in lowercase
def wordsToNum(word):
	ones = ['','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
	teens = ['','eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'];
	tens = ['', 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'];
	others = ['hundred', 'thousand', 'million'];
	words = word.split(' ');	#splits the input string of user and stores it in a list
	num = 0;	#initialize num to 0
	
	if word == 'zero':
		return num;
	else:
		temp = 0;	#temporary variable for storage of words found in ones
		for word in words:	#loops through all the words in the list
			if word == 'negative':
				print("\nNumber out of range!");
				break;
				
			elif word in ones:
				temp = ones.index(word);	#value is stored in temp
				num = num+ones.index(word);
				
			elif word in teens:
				num = num+(teens.index(word)+10);
				
			elif word in tens:
				num = num+(tens.index(word)*10);
				
			elif word in others:
				 if others.index(word) == 0:	#special case if 'hundred' is found
				 	num = num + (temp*100)-temp;	#previously found value of temp is multiplied by a hundred then subtracted by temp
				 elif others.index(word) == 1:
				 	num = num*1000;
				 else:
				 	num = num*1000000;
				 #end of else statement
			#end of elif statement
		#end of for loop
		
		if num > 1000000:
			print("\nNumber out of range!");
			return num;
		elif num >= 1:
			return num;
		#end of elif statement
	#end of else statement
#End of wordsToNum function


#-------------------------------------------------------------------------------------------------------------
#Accepts two arguments: the first argument is the number in word form (from zero to 1 million)
#and the second argument isany of the following: JPY, PHP, USD.
#The function returns the number in words to its numerical form with a prefix of the currency
def wordsToCurrency(word, currency):
	num = int(wordsToNum(word));
	curr = ['JPY', 'PHP', 'USD'];
	
	if currency not in curr:	#checks if the currency is not in the list
		print("\nCurrency not of scope!");
	#end of if statement
	
	if(num >=0  and num <= 1000000):
		if currency == 'JPY' or currency == 'PHP' or currency == 'USD':
			print("\nConversion: %s" % (currency + str(num)));
		#end of if statement
	#end of if statement
#End of wordsToCurrency function
	

#-------------------------------------------------------------------------------------------------------------
#Accepts three arguments: the first is the number from zero to 1 miliion,
#the second is the delimiter to be used (single character only)
#and third, the number of jumps when the delimiter will appear (from right most going to left most digit)
def numberDelimited(num, delimiter, jumps):
	if(num < 0 or num > 1000000):
		print("\nNumber out of range!");
	#end of if statement
	
	if(len(delimiter) > 1):
		print("\nInvalid number of delimiter!");
	#end of if statement
		
	if(jumps > len(delimiter)):
		print("\nNumber of jumps greater than length of number!");
	#end of if statement
	
	if(len(delimiter) == 1 and (num >= 0 and num <= 1000000) and (jumps < len(delimiter))):
		num = str(num);	#converts int to string
		digits = list(map(str, num));	#splits the number into digits and stores it
		index = len(num);	#gets the length of the number
		digits.insert(index-jumps, delimiter);	#insert delimiter into the jumps index from the right
		
		print("\nOutput: ");
		print(''.join(digits));	#prints a string in which the elements of the list has been joined by a space
	#end of if statement
#End of numberDelimited function


#-------------------------------------------------------------------------------------------------------------
#Function for printing the menu
def printMenu():
	choice = 5;	#initialize choice to 5
	
	while(choice != 0):	#while user has not chosen to exit, printMenu will continue to loop
		print("\n***********************************");
		print("*                                 *");
		print("*     [ 1 ] Number to words       *");
		print("*     [ 2 ] Words to number       *");
		print("*     [ 3 ] Words to currency     *");
		print("*     [ 4 ] Number delimited      *");
		print("*     [ 0 ] Exit                  *");
		print("*                                 *");
		print("***********************************");
	
		choice = int(input("Enter choice: "));

		if choice == 1:
			num = int(input("\nEnter a number from 0 to 100000: "));
			
			if(num >= 0 and num <= 1000000):	#checks if the input number is within the range of 0 to 1000000
				print("\nConversion: ");
				numToWords(num);
			else:
				print("\nNumber out of range!");
			#end else statment
			
		elif choice == 2:
			word = input("\nEnter a number(in word form): ");
			num = int(wordsToNum(word));
			
			if(num >= 0 and num <= 1000000):
				print("\nConversion: %d" % num);
			
		elif choice == 3:
			word = input("\nEnter a number(in word form): ");
			currency = input("Enter currency(JPY, PHP, USD): ");
			wordsToCurrency(word, currency);
			
		elif choice == 4:
			num = int(input("\nEnter a number from 0 to 100000: "));
			delimiter = input("Enter delimiter(single character only): ");
			jumps = int(input("Enter number of jumps: "));
			
			numberDelimited(num, delimiter, jumps);
			
		elif choice == 0:
			print("\nProgram Terminated...");
			
		else:
			print("\nInvalid input!");
		#end else statement
	#end of while loop
#End of printMenu function
	
printMenu();
