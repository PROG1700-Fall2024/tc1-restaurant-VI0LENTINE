#PROG 1700 – Tech Check #1
#Variables, Operators, Input/Output & Casting

# Restaurant Bill 
# You will create a console-based Python program that will calculate the amount of the tip, the tax, and the 
# total amount of a restaurant bill. The program will prompt the user to input the original amount of the bill. 
# The program will then output the amount of the tax (15% of the original amount) and a tip (20% of the original amount). 
# Finally, the program will output the new total of the bill.


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    user = input("Please put in your original bill amount: ")
    bill = float(user)
    tax = bill * 0.15
    tip = bill * 0.20
    total = bill + tax + tip
    print("Your original bill amount is: ", bill)
    print("Your tax is: ", round(tax,2))
    print("Your tip is: ", round(tip,2))
    print("Your total is: ", round(total,2))
    # YOUR CODE ENDS HERE

main()
