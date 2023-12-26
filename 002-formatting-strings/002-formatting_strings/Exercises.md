#### Review exercises:

- print a string that uses double quotation marks inside the string
- print a string that uses an apostrophe (single quote) inside the string
- print a string that spans across multiple lines: use triple quotes
- print a one-line string that you have written out on multiple lines: use '\' at EOL

---

- Create a string and print its length using the len() function
- Create two strings, concatenate them (add them next to each other) and
print the combination of the two strings
- Create two string variables, then print one of them after the other (with a
space added in between) using a comma in your print statement
- print the string “zing” by using subscripting and index numbers on the
string “bazinga” to specify the correct range of characters

---

- Write a script that takes input from the user and displays that input back
- Use CTRL+SPACE to view all the methods of a string object, then write a script that returns the lower-case version of a string

---

- Create a string object that stores an integer as its value, then convert that string into an actual integer object using int(); test that your new object is really a number by multiplying it by another number and displaying the result
- Repeat the previous exercise, but use a floating-point number and float()
- Create a string object and an integer object, then display them side-by-side with a single print statement by using the str() function

---

- Create a “float” object (a decimal number) named weight that holds the value 0.2, and create a string object named animal that holds the value“newt”, then use these objects to print the following line without using the format() string method:
  
    `0.2 kg is the weight of the newt.`
- Display the same line using format() and empty `{}` place-holders
- Display the same line using `{}` place-holders that use the index numbers of the inputs provided to the `format()` method
- Display the same line by creating new string and float objects inside of the `format()` method

---

##### Write a script “translate.py” that asks the user for some input with the following prompt: `Enter some text:`
You should then use the replace() method to convert the text entered by the user into “leetspeak” by making the following changes to lower-case letters:

 - The letter: a becomes: 4
 - The letter: b becomes: 8
 - The letter: e becomes: 3
 - The letter: l becomes: 1
 - The letter: o becomes: 0
 - The letter: s becomes: 5
 - The letter: t becomes: 7

Your program should then display the resulting output. A sample run of the program, is shown below:
  
    >>> Enter some text: I like to eat eggs and spam.
    I 1ik3 70 347 3gg5 4nd 5p4m.