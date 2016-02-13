def printMenu():
	choice = 5;
	
	while(choice != 0):
		print("***********************************");
		print("*                                 *");
		print("*     [ 1 ] Number to words       *");
		print("*     [ 2 ] Words to number       *");
		print("*     [ 3 ] Words to currency     *");
		print("*     [ 4 ] Number delimited      *");
		print("*     [ 0 ] Exit                  *");
		print("*                                 *");
		print("***********************************");
	
		choice = int(input("Enter choice: ")) #Asks what the user wants to do

		if choice == 1:
			print("1");
		elif choice == 2:
			print("2");
		elif choice == 3:
			print("3");
		elif choice == 4:
			print("4");
		elif choice == 0:
			print("\nProgram Terminated...");
		else:
			print("Invalid input!");
	
printMenu();
