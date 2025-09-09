# Eg 7th string notes

# a sring is just a sequence of symbols that are held together by quutaion marks
# stings can be defined using single quotes or double quotes
# example 
first_name = input("what is your first name: \n").strip().title()
last_name = input("what is your last name: \n").strip().title()
full_name = first_name + last_name



sentence = 'The quick brown fox jumps over the lazy dog.          '.strip()

print(sentence.find("jumps"))
print(sentence[20:25])
print(sentence[sentence.find("lazy"): len("lazy")+sentence.find("lazy")]) # this is slicing 
print(len(first_name)) # finds length of string
print('welcome to my program', first_name, last_name +"!")




#concatanate is joining two or more strings together
#sanitization and stupid profing
#stupid profing is making sure that the user doesnt break your code
#sanitization is step one of stupid profing
#debugging takes forever
# bug is an error in your code
# there are 3 types of bugs 
# 1. syntaxt error is a mistake in your grammer.
# couses of syntax error are spaces missplelling forgeting a comma or =.
# 2. logic error - 1 + 2 = 12 # its a mistake in your logic
# 3. runtime error - when your code looks fine but when you run it breaks
# it runs until it hits the error
# index counts starting from 0




#debugging is fixing code