### SET 00: pre

1. find sum of all natural numbers between 1 to n
    ```python
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(sum(numbers))
    ```

2. count number of digits in a number
    ```python
    number = 12345
    print(len(str(number)))
    ```

3. print first and last digit of a number
    ```python
    number = 12345

    convert = str(number)
    print('last :', convert[-1], number%10)
    print('first:', convert[0], number//(10**(len(convert)-1)))
    ```

4. find sum of first and last digit of a number
    ```python
    number = 12345
    
    num = str(number)
    print('first + last:', num[0] + num[-1])
    print('first + last:', int(num[0]) + int(num[-1]))
    print('first + last:', sum([int(num[0]), int(num[-1])]))
    ```

5. swap first and last digits of any number
    ```python
    number = 12345
    
    num = str(number)
    print('swap:', num[-1] + num[1:-1] + num[0])
    ```

6. print number in reverse
    ```python
    number = 12345
    
    num = str(number)
    print(num[::-1])
    print(''.join(reversed(num)))
    print(*reversed(num), sep='')
    ```

7. find factorial of given number
    ```python
    n = 4
    
    f = 1
    for i in range(1, n+1):
        f *= i

    print(f)
    ```

8. print multiplication table of any number.
    ```python
    n = 2
    
    for i in range(5):
        print(i, 'x', n, '=', i-n)
    ```

9. count digits, alphabets and others in given string
    ```python
    string = "this is python 3.7"
    
    alpha = numb = others = 0

    for c in string:
        if   c.isalpha(): alpha += 1
        elif c.isdigit(): numb  += 1
        else: others += 1

    print('alpha', alpha)
    print('numb', numb)
    print('others', others)
    ```

### SET 01: intro

1. check string whether its palindrome or not.
    ```python
    रहर, मलम, नयन, hannah, racecar

    word = "नयन"
    python  :results output
    print(word == word[::-1])
    print('Yes' if word == ''.join(reversed(word)) else 'No')
    ```

2. check if number is prime or not
    ```python
    def isPrime(n):
        if n == 1: return False
        for x in range(2, n):
            if n % x == 0: return False
        return True

    print(isPrime(2))
    print(isPrime(5))
    print(isPrime(8))
    ```

3. print pattern
    ```python
    for i in range(5):
        for j in range(5):
            print('*', end=' ')
        print()
    ```

    ```python
    for i in range(5):
        for j in range(5):
            if i > j: print(end='  ')
            else: print('*', end=' ')
        print()
    ```

4. convert a binary string into decimal integer?
    ```python
    sample = "10101"
    
    print(int(sample, 2))
    ```

5. calculate sum of digits of any number
    ```python
    num = 12345
    
    s = 0
    for d in str(num):
        s += int(d)

    print('sum:', s)
    ```

    ```python
    s = 0
    while num > 0:
        s    += num%10
        num //= 10

    print('sum:', s)
    ```

6. find all number between 0 to 1000 which are base 2, 8, 10 palindrome
    ```python
    count = 0
    for n in range(1000):
        d = str(n)
        if d != d[::-1]: continue
        b = bin(n)[2:]
        if b != b[::-1]: continue
        o = oct(n)[2:]
        if o != o[::-1]: continue
        print(n, bin(n), oct(n))
        count += 1
    print(count)
    ```

7. print fibonacci series up to n terms
    ```python
    n = 10
    
    f1 = 0
    f2 = 1
    for f in range(n):
        print(f1, end=' ')
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    ```

### SET 02: basic

1. print all english alphabets
    ```python
    for i in range(ord('a'), ord('z') + 1):
        print(chr(i-32) + chr(i), end=' ')
    ```

2. print all devnagari consonants
    >0x915 → क
    ```python
    for i in range(37):
        print(chr(i + 0x915), end=' ')
    ```

3. what month it would be, given the number of month.
    ```python
    month = 15
    
    m = month%12
    print(m)

    import calendar
    print(list(calendar.month_name)[m])
    ```

4. how many 2-digit number have tens digit smaller than units digit
    ```python
    numbers = []
    for i in range(10, 100):
        tens, ones = divmod(i, 10)
        if tens < ones:
            numbers.append(i)

    print(numbers[:5])
    print(len(numbers))
    ```

5. encrypt the message with Caesar Cipher
    #### WIP

6. find the number of lines in the file
    ```python
    count = 0
    with open('exercises.org') as fp:
        # for line in fp.readlines():
        for line in fp:
            count += 1
    print(count)

    print(open('exercises.md').read().count('\n'))

    import os
    os.system('wc -l exercises.org')
    ```

7. print 10-20 lines of the file
    ```python    
    count = 0
    with open('exercises.org') as fp:
        # for line in fp.readlines():
        for line in fp:
            count += 1
            if 10 <= count <= 20:
                print(line)

    print(count)
    print(open('exercises.org').read().split('\n')[10:20])
    ```

8. find the number of char in the file
    ```python    
    count = 0
    with open('exercises.md') as fp:
        for line in fp.readlines():
            count += len(line)

    print(count)

    count = 0
    with open('exercises.md') as fp:
        print(fp.tell())
        for line in fp:
            count += 1
        print(fp.tell())
    print(count)

    import os
    print(os.path.getsize('exercises.md'))
    ```

9.  find the number of words in the file
    ```python    
    with open('exercises.org') as fp:
        data = fp.read()

    print(len(data.split()))
    ```

10. digit count
    ```python
    num = 11235813 :results output
    freq = dict()

    while num > 0:
        num, r = divmod(num, 10)
        freq[r] = freq.get(r, 0) + 1

    print(*freq.items(), sep='\n')
    ```
    
11. find HCF (GCD) of two numbers
    #### WIP

12. Magic square

    -------------
    | 8 | 1 | 6 | → 15 = 8 + 1 + 6
    - - - - - - -
    | 3 | 5 | 7 | → 15 = 3 + 5 + 7
    - - - - - - -
    | 4 | 9 | 2 | → 15 = 4 + 9 + 2
    -------------
    15  15  15

    D1: 8 + 5 + 2 = 15
    D2: 6 + 5 + 4 = 15

    Magic square is an arrangement of distinct numbers (i.e., each number
    is used once), usually integers, in a square grid, where the numbers
    in each row, and in each column, and the numbers in the main and
    secondary diagonals, all add up to the same number, called the "magic
    constant".

13. find LCM of two numbers
    #### WIP

14. print pascal triangle


    for i in range(5):
        print(' '*(5-i), end='')  # leading spaces.
        for j in range(1, i+2):   # generate 1 through peak value.
            print(j, end='')
        for j in range(i, 0, -1): # generate peak - 1 through 1.
            print(j, end='')
        print()
    
      1
     121
    12321
   1234321
  123454321

    Featurs of pascal triangle

    
        for i in range(1, 6):
            for j in range(1, 6):
                if i < 6 - j:
                    print(end=' ')
                    continue
                print(i, end=' ')
            print()
    
    :     1
    :    2 2
    :   3 3 3
    :  4 4 4 4
    : 5 5 5 5 5

matter of life and death

- SET 03: primer

1. count digit frequency

    python  num = 11235813 :results output
    # string ways
    freq = dict()
    for n in str(num):
        freq[n] = freq[n] + 1 if n in freq.keys() else 1
        # if n in freq.keys():
        #     freq[n] = freq[n] + 1
        # else:
        #     freq[n] = 1
    print(sorted(freq.items()))

    # math ways
    freq = dict()
    n = num
    while n > 0:
        r = n%10
        freq[r] = freq.get(r, 0) + 1
        n //= 10
    print(sorted(freq.items()))
    
    : [('1', 3), ('2', 1), ('3', 2), ('5', 1), ('8', 1)]
    : [(1, 3), (2, 1), (3, 2), (5, 1), (8, 1)]

2. sort following dictionary according to

    
    a = {
        "one"   : 1,
        "three" : 3,
        "two"   : 2,
        "four"  : 4,
    }
    
    - to value
    - lenght of key

    
    a = dict(zip(("one", "two", "three", "four"), range(1, 5)))

    print(sorted(a))                       # by key
    print(sorted(a.items()))               # by key and show value too
    print(sorted(a, key=lambda k: a[k]))   # by value
    print(sorted(a, key=lambda k: len(k))) # by length

    
    : ['four', 'one', 'three', 'two']
    : [('four', 4), ('one', 1), ('three', 3), ('two', 2)]
    : ['one', 'two', 'three', 'four']
    : ['one', 'two', 'four', 'three']

3. frequency of char in /usr/share/dict/words

4. find top 5 words used in file

    
    freq = {}
    for word in open('exercises.org').read().split():
        freq[word] = freq.get(word, 0) + 1

    print(sorted(freq.items(), key=lambda k: k[1], reverse=True)[:5])
    
    : [(':', 118), ('=', 95), ('in', 67), ('-', 59), ('#+BEGIN_SRC', 52)]

5. word length distribution of /usr/share/dict/words

    
    freq = dict()

    with open('/usr/share/dict/words') as fp:
        for line in fp.readlines():
            l = len(line.strip())
            freq[l] = freq.get(l, 0) + 1

    print(freq)
    
    : {1: 52, 2: 491, 3: 1463, 6: 12805, 8: 18872, 7: 17213, 9: 17638, 10: 14621, 5: 7613, 4: 3939, 11: 11130, 13: 4586, 12: 7505, 14: 2522, 16: 684, 18: 129, 15: 1410, 17: 338, 20: 20, 22: 8, 19: 64, 21: 9, 23: 2, 24: 1}

6. word length range distribution

    1-2, 3-4, 5-6

    
    freq = dict()

    with open('/usr/share/dict/words') as fp:
        for line in fp.readlines():
            l = len(line.strip())
            freq[l] = freq.get(l, 0) + 1

    print(freq)

    f = iter(list(freq.items()))
    group = dict()
    for x, y in zip(f, f):
        key = '{[0]}-{[0]}'.format(x, y)
        group[key] = x[1] + y[1]

    print(group)
    
    : {1: 52, 2: 491, 3: 1463, 6: 12805, 8: 18872, 7: 17213, 9: 17638, 10: 14621, 5: 7613, 4: 3939, 11: 11130, 13: 4586, 12: 7505, 14: 2522, 16: 684, 18: 129, 15: 1410, 17: 338, 20: 20, 22: 8, 19: 64, 21: 9, 23: 2, 24: 1}
    : {'1-2': 543, '3-6': 14268, '8-7': 36085, '9-10': 32259, '5-4': 11552, '11-13': 15716, '12-14': 10027, '16-18': 813, '15-17': 1748, '20-22': 28, '19-21': 73, '23-24': 3}


- PROJECT 02: convert decimal number to roman


from demo import roman

print(roman.convert(2))
print(roman.convert(64))
print(roman.convert(1024))

print(roman.letterMap)


: II
: LXIV
: MXXIV
: [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

- PROJECT 03: convert number to words
- SET 04: not so basic
-- Python program to find LCM of two numbers

Least Common Multiple

    a=15 b=20

    def gcd(a,b):
        if a == b: return a
        if a >  b: return gcd(a-b, b)
        return gcd(a, b-a)

    print('GCD:', gcd(a,b))
    print('LCM:', (a-b) / gcd(a,b))


: GCD: 5
: LCM: 60.0


# This code is contributed by Danish Raza

- SET 05: modules

1. cos(5.6 - 7.3j)

-- Date and Time

1. print yesterday, today, tomorrow
2. drop microseconds from datetime
3. difference in dates, days, hours, minutes, seconds
4. calculate an age for given year.
- PROJECT 04 pong
- PROJECT 05 binary world
- PROJECT 06 meme generator
- PROJECT 07 send email
- SET 06: map/reduce/filter and list comprehension
-- basic

1. Take vectors multiply by constant
    # 5 - [ 1, 2, 3 ] =

2. Count each char of the word and put in list
    'the quick brown fox jumps over the lazy dog'

3. Removing vowels from a sentence

    
    def eg2_for(sentence):
        vowels = 'aeiou'
        filtered_list = []
        for l in sentence:
            if l not in vowels:
            filtered_list.append(l)
        return ''.join(filtered_list)
    
4. print all english alphabets

5. put commas in the numbers

6. key value pair

    
    country = ['Bangladesh', 'Bhutan', 'India', 'Pakistan', 'Nepal' ]
    capital = ['Dhaka', 'Thimphu', 'New Delhi', 'Islamabad','Kathmandu',  ]
    
-- intermedated

1. Take a matrix as input and return a list with each row placed
    on after the other.

    
    def flatten(matrix):
        flat = []
        for row in matrix:
            for x in row:
                flat.append(x)
        return flat

    flat = flatten([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])

    print(flat)
    
        : [1, 2, 3, 3, 4, 5, 6, 7, 8]

    [ x for row in matrix for x in row ]

2. Multiply the 3 row and 3 column vector

    [ 1, 2, 3 ] [[1],[2],[3]]

- SET 07: generator
- SET 08: strings

1. Read file prints the lines all characters in the sentence capitalized.

    Hello world
    Practice makes perfect

    Then, the output should be:

    HELLO WORLD
    PRACTICE MAKES PERFECT

2. find top 5 most used word from the your program itself.

    
    data = open('Exercises.org').read().lower().split()
    freq = dict()
    for w in data:
        freq[w] = freq[w] + 1 if w in freq else 1
    print(-sorted(freq.items(), key=lambda k: k[1] , reverse=True)[:5], sep='\n')
    
    : ('=', 30)
    : ('number', 26)
    : (':', 24)
    : ('of', 22)
    : ('print', 22)

3. read xml file
4. read csv file
5. date string in dd-mm-yyyy format return back a day, month and
    year

- SET 09: dynamic programming

1. fibonacci sequence recursion

- SET 10: metaclass

- What are metaclasses in Python?
- What is monkey patching? How to use in Python? Example?
-

- SET 11: regex

1. the set of all alphabetic strings.

    [A-Za-z]+

2. the set of all lowercase alphabetic strings ending in ab.

    [a-z]-ab

3. the set of all strings with two or consecutive repeated words

    ([[:alpha:]].-){2}

4. the set of all strings from the alphabet a, b such that each a is
    immediately preceded and immediately followed by ab.


5. validate if password meets following criteria
    - At least 1 one upper case and lower case letters
    - At least 1 number between and symbol
    - Minimum length of password: 6

    Example:

    If the following passwords are given as input to the program:
    ABd1234@1,a F1#,2w3E-,2We3345
    Then, the output of the program should be:
    ABd1234@1

    python
    import re
    value = []
    items=[x for x in input().split(',')]
    for p in items:
    if len(p)<6 or len(p)>12: continue
    else: pass
    if not re.search('[a-z]',p): continue
    elif not re.search('[0-9]',p): continue
    elif not re.search('[A-Z]',p): continue
    elif not re.search('[$#@]',p): continue
    elif re.search('\s',p): continue
    else: pass
    value.append(p)
    print ','.join(value)
    
6. verify the email address

- SET 12: search

1. binary search

- SET: turtle
-- Basic
2. Generate Color Pallet Mix RGB color
    
    color((<int:red>, <int:green>, <int:blue>))
    3. analog clock
4. Sierpiński triangle
5. Sierpiński carpet

- not so basic

1. check palindrome lambda function

    
    isPalindrome = lambda w: w == w[::-1]
    print(isPalindrome('hannah'))
    isPalindrome_free_case = lambda w: w.lower() == w[::-1].lower()
    print(isPalindrome_free_case('DammitImMad'))
    
    : True
    : True

- etc

1. find two's complement of a binary number.
    
    def twos_complement(value):
        mask = 2--(len(bin(value)) - 3)
        return -(value & mask) + (value & ~mask)

    print(twos_complement(10))
    
    : -6

- PROJECTS

5. 15-puzzle game
7. Snake

- TRICKY
-- Passing empty list in the function


    def extendList(val, lst=[]):
        lst.append(val)
        return lst

    lst = extendList(10)
    print(lst)                # [10,'a']
    print(extendList(123,[])) # [123]
    print(extendList('a'))    # [10, 'a']
    print(lst)                # whats it value


: [10]
: [123]
: [10, 'a']
: [10, 'a']

-- Late Binding


    def multipliers():
        return [lambda x : i - x for i in range(4)]

    print([m(2) for m in multipliers()])


: [6, 6, 6, 6]

if your answer is [0, 2, 4, 6] then its wrong

-- Method Resolution Operator


    class Parent(object):
        x = 1

    class Child1(Parent):
        pass

    class Child2(Parent):
        pass

    print(Parent.x, Child1.x, Child2.x)
    Child1.x = 2
    print(Parent.x, Child1.x, Child2.x)
    Parent.x = 3
    print(Parent.x, Child1.x, Child2.x)


: 1 1 1
: 1 2 1
: 3 2 3

-- indexing in list

list = ['a', 'b', 'c', 'd', 'e']
print(list[10:])  # []

-- Referencing same memory location
1. list = [ [ ] ] - 5
2. list  # output?
3. list[0].append(10)
4. list  # output?  #[[10],[10],[10],[10],[10]]
5. list[1].append(20)
6. list  # output?  #[[10,20],[10,20],[10,20],[10,20],[10,20]]
7. list.append(30)
8. list  # output?  #[[10,20],[10,20],[10,20],[10,20],[10,20],30]
