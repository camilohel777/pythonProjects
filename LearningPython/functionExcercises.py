#checks if input is an int
def is_int(x):
    if x - int(x) == 0:
        return True
    else:
        return False
    
print is_int(8.9)

#adds every digit of the number
def digit_sum(n):
    x = str(n)
    result = 0
    for char in x:
        result += int(char)
    return result   
    
print digit_sum(1234)

#gets factorial of the number
def factorial(x):
    n = x - 1
    while n > 0:
        x *= n 
        n-=1
    return x
    
print factorial(4)

#returns true if number is prime
def is_prime(x):
    n = x/2
    counter = 1
    while n > 0:
        if x%n == 0:
            counter+=1
        n-=1
    if counter < 3 and x > 1:
        return True
    else:
        return False

print is_prime(4)            

#returns the string reversed
def reverse(text):
    rev = []
    for char in text:
        rev.insert(0,char)
    text = ''.join(rev)
    return text
print reverse('abcd')
    
# auxillary function to check is character is a vowel
def is_vowel(char):
    if 'a' == char.lower():
        return True   
    elif 'e' == char.lower():
        return True  
    elif 'i' == char.lower():
        return True  
    elif 'o' == char.lower():
        return True  
    elif 'u' == char.lower():
        return True    
    else :
        return False
        
#function to remove vowels from text
def anti_vowel(text):
    result = ""
    for char in text:
        if is_vowel(char) == True:
            result += ""
        elif is_vowel(char) == False:
            result += char
        else:
            result+= " "
    return result
        
print anti_vowel("Hey You!")   

#Scrabble score function
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
    total = 0
    for char in word:
         total += score[char.lower()]
    return total 

print scrabble_score("Helix")

#censoring a word in a text
def censor(text, word):
    counter = 0
    censored =""
    for i in range(len(word)):
        censored += "*"
    result =""
    for i in range(1 + len(text) - len(word)+1):
        if text[i:i + len(word)] == word:
            counter += 1
    
    result = text.replace(word, censored,counter)
    return result
           
print censor("this hack is wack hack", "hack")    
    
# Returns number of times that item is in the sequence list
def count(sequence, item):
    counter = 0
    for i in sequence:
        if i == item:
            counter += 1
    return counter
               
print count([1,2,1,1], 1)        
print 

#Removes odd number from a list
def purify(sequence):
    result = []
    for i in range(0, len(sequence)):
        print sequence[i]
        if sequence[i]%2 == 0:
            result.append(sequence[i])
    return result
    
print purify([4, 5, 5, 4])
print

#product of whole list
def product(intlist):
    product = 1
    for i  in intlist:
        product *= i
    return product

print product([4, 5, 5])    

#removes duplicates in a list
def remove_duplicates(lst):
    result = list(set(lst))
    return result
        
print remove_duplicates([1,1,2,2])    
    
#median of the list
def median(lst):
    lst = sorted(lst)
    if len(lst) % 2 == 0:
        median = (lst[len(lst)/2 ] + lst[len(lst)/2 -1])/2.0
    else:
        median = lst[len(lst)/2]
    return median
    
print median([7,3,1,4])
print median([1,2,3,4,5])   