#Detecting Plagiarism in a string.



# Importing SequenceMatcher
# from difflib module
from difflib import SequenceMatcher

# Declaring string variables
string1 = 'I am geek'
string2 = 'I am geeks'

# Using the SequenceMatcher()
match = SequenceMatcher(None,string1, string2)

# convert above output into ratio
# and multiplying it with 100
result = match.ratio() * 100

# Display the final result
print(int(result), "%")






#Creating Plagiarism Detection in Python for Text Files

# importing SequenceMatcher of difflib module
from difflib import SequenceMatcher

with open('doc1.txt') as first_file,
	open('doc2.txt') as second_file:
	
	# Reading Both Text Files
	file1 = first_file.read()
	file2 = second_file.read()
	
	# Comparing Both Text Files
	ab = SequenceMatcher(None, file1,
						file2).ratio()
	
	# converting decimal output in integer
	result = int(ab*100)
	print(f"{result}% Plagiarized Content")
