# Homework 4 - 6/23/20
# Lists, Nested Loops, String Manipulation, Indexes

# Terminal commands:
# python hw4_tests.py
# or 
# python hw4_submission.py

# Blitz Problem: for loops
# Change all the words (verbs) in the list from present to past tense ( add -ed). Return the 
# modified verbs list.
# Hint: Use a range for loop with indeces, not a for-each loop.
def blitz():
    verbs = ["wait", "exit", "break", "create", "seem", "control", "bool", "cook"]
    # Your code starts here.
    for x in range(0, len(verbs)):
        verbs[x] += "ed"
    return verbs

print ( blitz() )

# (Medium) Write the code for two functions, swap() and manualReverse().

# printBox()
# Returns a string, which looks like a box made of "*" chars, with dimensions height and width.
# Hint: This requires a nested for loop, but there is no list.
# Hint 2: Add a "\n" char after each line. This is equivalent to pressing Enter.
def printBox(height, width):
    # Your code starts here.
    line = ""
    for y in range(0, height):
        for x in range(0, width):
            line += "*"
        line += '\n'
    return line
    
print ( printBox(5, 4) )


# But what happens if we have a list, and in each index of the list, is another list?
# This creates a 2-D array, or a n x m matrix, where n and m are the lengths of the lists.

# For this problem, I've started the matrix for you, but its empty.
# I want you to check to see if my matrix is the identity matrix, which looks like this:
# n = 3:
# [1] [0] [0]
# [0] [1] [0]
# [0] [0] [1]
# Return False once you know the matrix is not an identity matrix.
# If there are no errors and the matrix is valid, return True
def checkMatrix(matrix):
    n = len(matrix)
    # Your code starts here.
    for y in range(0, n):
        for x in range(0, n):
            if( ((x == y) and (matrix[y][x] != 1)) or ((x != y) and (matrix[y][x] != 0)) ):
                return False
    return True

matrix = [ [1, 0, 0], [0, 1, 0], [0, 0, 1] ]
print ( checkMatrix(matrix) )