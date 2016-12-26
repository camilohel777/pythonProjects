#Pig latin translator
pyg = 'ay'
original = raw_input("Enter a word: ")

#Get the original word, move the first letter to the end and then append 'ay' to the end
#if statements check that string is not empty and that it does not contain characters that aren't letters
if len(original) > 0 and (original.isalpha()):
    
    print original
    word = original.lower()
    first = original[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print new_word
    
else:
    print "empty" 
    
