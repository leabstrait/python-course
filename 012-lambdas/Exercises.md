##### A lambda function to return formatted fullname, given first name and last name
```python
full_name = lambda first, last: f'Full name: {first.title()} {last.title()}
full_name('guido', 'van rossum')
```

##### Swapper
```python
swap = lambda x, y: y, x
x = 1
y = 2
x, y = swap(x, y)
```

##### Count numbers of odds and even nums
```python
# list of numbers 
list1 = [10, 21, 4, 45, 66, 93, 11] 
  
odd_count = len(list(filter(lambda x: (x%2 != 0) , list1))) 
  
# we can also do len(list1) - odd_count 
even_count = len(list(filter(lambda x: (x%2 == 0) , list1))) 
  
print("Even numbers in the list: ", even_count) 
print("Odd numbers in the list: ", odd_count) 

```

##### Function to find intersection of two arrays 
```python
def interSection(arr1,arr2): 
  
     # filter(lambda x: x in arr1, arr2)  --> 
     # filter element x from list arr2 where x 
     # also lies in arr1 
     result = list(filter(lambda x: x in arr1, arr2))  
     print ("Intersection : ",result) 
  
# Driver program 
if __name__ == "__main__": 
    arr1 = [1, 3, 4, 5, 7] 
    arr2 = [2, 3, 5, 6] 
    interSection(arr1,arr2) 

```


```python
# Python code demonstrate the working of 
# sorted() with lambda 
  
# Initializing list of dictionaries 
lis = [{ "name" : "Nandini", "age" : 20},  
{ "name" : "Manjeet", "age" : 20 }, 
{ "name" : "Nikhil" , "age" : 19 }] 
  
# using sorted and lambda to print list sorted 
# by age  
print "The list printed sorting by age: "
print sorted(lis, key = lambda i: i['age']) 
  
print ("\r") 
  
# using sorted and lambda to print list sorted  
# by both age and name. Notice that "Manjeet" 
# now comes before "Nandini" 
print "The list printed sorting by age and name: "
print sorted(lis, key = lambda i: (i['age'], i['name'])) 
  
print ("\r") 
  
# using sorted and lambda to print list sorted 
# by age in descending order 
print "The list printed sorting by age in descending order: "
print sorted(lis, key = lambda i: i['age'],reverse=True) 
```