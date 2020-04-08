"""
STATE VARIABLES
- accumulator
- flags
- control variables/sentinel variables

PURPOSE: To keep track of something. Maybe a quantity, or whether certain event has happened

"""
# Example
# keep asking the user whether he wants to enter numbers (y for yes, anything else is no)
# add up all the numbers that the user has keyed in
# note: don't use a list

total = 0
keep_going = True
 
#precondition: 
#total must be the sum of all the numbers so far
#keep_going is True if itis at the start of the program or if the user enters 'y' for the previous iteration
while keep_going:
    n = int(input("Enter a number "))
    total += n  #total = total + n
    keep_going = input("Enter more numbers? (y/n)") == "y"

