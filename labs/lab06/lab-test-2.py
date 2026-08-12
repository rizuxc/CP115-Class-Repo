#Programmer's name: AHMAD RIZKY BIN SOHIPIN
#Problem description: Print student's information, the letter "K" using star symbol, the student's demanded marks, and indentation.

#These 2 lines of codes takes the inputs given by user to display their informations later on.
name = str(input("Name: "))
matricno = str(input("Matric. No: "))

#This 3 lines of codes performs the arithmetic operations for the mark.
mark1 = 2
mark2 = 10
tMark = mark1 * mark2

#This shows the output.
print(f"Name: {name}\t\tMatric. No: {matricno}\n" #This line of code displays the student's informations.
      f"*\t\t\t*\n"
      f"**\t\t**\n"
      f"***\t***\n"
      f"********\n"
      f"***\t***\n"
      f"**\t\t**\n"
      f"*\t\t\t*\n"
      f"\n"
      f"\n"
      f"This is my\n"
      f"\tsecond\n"
      f"\t\tassignment\n"
      f"I want {mark1}x{mark2} marks, which is {tMark} full marks")