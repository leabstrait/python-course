# Basic Python Course
This course is geared towards beginners in The Python Programming Language and programming in general. It assumes no experience apart from knowing how to operate and install software in a computer.

```python
import antigravity
```


## Setting up a development environment
The best development environment is the one that suits the programmer's particular needs. This includes selection of text editors or IDEs, themeing, shell, plugins and extensions and even positioning of windows in the screen. It is recommended to use virtual environments for developing python projects. I recommend `pipenv` as an up and coming environment manager for developing in python.


## Command Line Environment
Based on the Linux Shell, basic commands are introduced for navigation, file / folder management, utilities


### The minimum basic commands
- uname
- pwd
- ls
- cd
- mkdir & rmdir
- touch
- cp
- locate 
- which
- mv
- rm
- man & --help
- grep
- echo
- cat
- nano / vi
- sudo
- df 
- du
- tar -cvf -xvf -tvf
- zip unzip
- chmod
- hostname
- ping


## Version Control with `git`

`git` is a distributed version control systemin use by many software development teams around the world. It was created by Linus Torvalds of Linux

### Configuration
```shell
git config --global user.name "username"
git config --global user.email "username@example.com"
```

### Usage
```shell
git init
```

- the `.git` folder

- the `.gitignore` file

```shell
git status
```

```shell
git add
```

```shell
git commit -m "COMMIT_MSG"
```

```shell
git log [--oneline]
```

```shell
git checkout
```


## The Python Programming Language - Topics

- Guido van Rossum - 1980s - 1991 release
- Named after Monty Python
- Compiled(*PVM*) and Interpreted both but let's stick with interpreted for now.
  
```python
>>> import this
```
- Python 3, around 2009

>  Some changes in Python 3.0:
>  - Print is now a function
>  - Views and iterators instead of lists
>  - The rules for ordering comparisons have been simplified. E.g. a heterogeneous list cannot be sorted, because all the elements of a list must be comparable to each other.
>  - There is only one integer type left, i.e. int. long is int as well.
>  - The division of two integers returns a float instead of an integer. "//" can be used to have the "old" behaviour.
>  - Text Vs. Data Instead Of Unicode Vs. 8-bit

- Typing Discipline
> Python is strongly, dynamically typed.
> - Strong typing means that the type of a value doesn't change in unexpected ways. A string containing only digits doesn't magically become a number, as may happen in Perl. Every change of type requires an explicit conversion.
> - Dynamic typing means that runtime objects (values) have a type, as opposed to static typing where variables have a type.

- Python Interpreter, REPL

- Data Types
  - Strings
    - String Formatting, *f*-strings
  - Number Types (Integers & Floats)

- Keywords & Builtins
```python
>>> import keyword
>>> keyword.kwlist
```
```python
>>> import builtins
>>> dir(builtins)
```

- Lists, Tuples and Sets

- Accessing and Slicing

- Conditionals and Booleans - if, elif, else 
  
- Dictionaries - Key: Value pairs
  
- Indentation Matters
  
- Loops and Iterations - for, while
  - break and continue

- Functions
  - Methods vs Functions
  - Arguments vs Parameters -> arguments are passed into a method's parameters
  - non arguments 
  - args, kwargs, defaults
  - *args(tuple), **kwargs(dict)
  - *arg_parameter, **kwarg_parameter
  - """docstrings"""

- Generators
  
- Comprehensions
  - List
  - Dict
  - Set
  - Generator
  
- Python's module system and The Standard Library
    - `pizza` module example
    - `os` module
    - `datetime` module
   
  **More stdlib modules**
    - `random` module
    - `csv` module
    - `json` module

- Variable Scope
  - LEGB Rule

- File I/O
    - Automate parsing and renaming of multiple files

- Error Handling
  - try / except / else / finally
  
- Functional Programming
  - First Class Functions
  - Higher Order Functions
  - Closures

- Decorators
  - Decorators on functions
  - Decorator Chaining
  - Decorator with arguments
  - Class Decorators  
  
- Object oriented Programming
  - Classes and Instances
  - Class Variables
  - classmethods and staticmethods
  - Inheritance 
  - Special / Magic methods `__method__`
    - `__str__()`
    - `__repr__()`
  - Property Decorators

- pip - pip installs packages
  - pip help
  - pip search PACKAGE
  - pip list 
  - pip list --outdated
  - pip install PACKAGE
  - pip install -U
  - pip freeze --local | grep -v `^\-e' | cut -d = -f 1 | xargs -n1 pip install -U
  - pip freeze
  - pip install -r requirements.txt
  - pip uninstall

- Databases
  - SQLite: Connection, Querying
  - Using functions to run queries
  - Explain ORM

- Logging
  - Logging levels
  - Log Formatting
  - Loggers

- Testing your Code
  - unittest module

- Context Managers
  
- Iterators and Iterables
  
- Multithreading
  
- Multiprocessing

## Paths you may take next

- Web Development
  - APIs
  - Routing
  - Database and ORMs
  - Views
  - Framework of Choice (Flask)

- Data Science and Analytics
  - Data Fetch
    - APIs
    - Scraping
  - Visualization
    - Libraries
  - Insights
    - Algorithms for Machine Learning