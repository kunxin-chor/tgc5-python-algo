"""
Given a list of names, print "exist" if the name "Alan" is in the list.
You are not allowed to use any list methods (no indexof)
"""

# think of a list as multiple variables sharing the same name
# the computer is BINARY MACHINE -- meanings it can only compare 2 things at time.
# and is most efficient when comparing two things at a time
names = ['David', 'Aaron', 'Nancy', "Sebanistan", "Windy", "Ivan"]

# linear search
for current_name in names:
    # filtering critera -- that's a IF statement to determine if the current item that we are looking at matches the critera
    if current_name == 'Alan':
        print("exist")
