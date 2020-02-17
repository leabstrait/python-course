```python
# Find all of the numbers from 1-1000 that are divisible by 7
results = [num for num in range(1000) if num % 7 == 0]
#print(results)


#Find all of the numbers from 1-1000 that have a 3 in them
results = [num for num in range(1000) if '3' in list(str(num))]
#print(results)

#Count the number of spaces in a string 
teststring = 'Find all of the words in a string that are less than 4 letters'
#print teststring.count(' ')   # normally I'd just do this, but for the practice....
results = [character for character in teststring if character == ' ']
#print(len(results))

#Remove all of the vowels in a string [make a list of the non-vowels]
teststring = 'Find all of the words in a string that are less than 4 letters'
vowels = ['a','e','i','o','u',' ']
results = [letter for letter in teststring if letter.lower() not in vowels]
#print(results)

#Find all of the words in a string that are less than 4 letters
teststring = 'Find all of the words in a string that are less than 4 letters'
results = [word for word in teststring.split() if len(word) < 4]
#print(results)

# CHALLENGE!
#Use a dictionary comprehension to count the length of each word in a sentence.
sentence = 'Use a dictionary comprehension to count the length of each word in a sentence'
results = {word:len(word) for word in sentence.split()}
#print(results)

#Use a nested list comprehension to find all of the numbers from 1-1000 that 
#are divisible by any single digit besides 1 (2-9)
# comprehension testing truth for divisibilty: [True for divisor in range(2,10) if number % divisor == 0]
results = [number for number in range(1,1001) if True in [True for divisor in range(2,10) if number % divisor == 0]]
#print(results)

#For all the numbers 1-1000, use a nested list/dictionary comprehension to 
#find the highest single digit any of the numbers is divisible by.
# List comprehension for providing a list of all of the numbers a number is divisible by: divisor_list:
#       [divisor for divisor in range(1,1001) if number % divisor == 0]
results = {number:max([divisor for divisor in range(1,10) if number % divisor == 0]) for number in range(1,1001)}
#print(results)

# From the given dictionary, filter out the fruits and store in another dictionary
stuff = {
    'mango': 'fruit',
    'apple': 'fruit',
    'cauli': 'vegetable',
    'potato': 'vegetable',
    'rice':'grain',
    'wheat':'grain'
}
{stuff: variant for stuff, variant in stuff.items() if variant=='fruit'}

# Python program to print odd Numbers in a List 
   
# list of numbers 
list1 = [10, 21, 4, 45, 66, 93, 11] 
   
only_odd = [num for num in list1 if num % 2 == 1] 
odd_count = len(only_odd) 
   
print("Even numbers in the list: ", len(list1) - odd_count) 
print("Odd numbers in the list: ", odd_count) 


# Function to rearrange positive and negative elements 
def Rearrange(arr): 
  
    # First lambda expression returns list of negative numbers 
    # in arr. 
    # Second lambda expression returns list of positive numbers 
    # in arr. 
    return [x for x in arr if x < 0] + [x for x in arr if x >= 0] 
  
# Driver function 
if __name__ == "__main__": 
    arr = [12, 11, -13, -5, 6, -7, 5, -3, -6] 
    print Rearrange(arr) 

```

