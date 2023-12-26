# PYTHON PREPARATION

# 1ST DIFRRENCE BETWEEN LIST AND TUPLE

## -LIST ARE MUTABLE

## -LIST IA A CONTAINER THAT CONTAIN DIFFRENT TYPES OF OBJECT

## -SYNTAX => LIST=[" 'A','B','C','1','2','3' "]

## -LIST ITRATION IS SLOWER

## -LIST CONSUME MORE MEMORY

## -OPERATION LIKE INSERTION AND DELETION ARE BETTER PERFORMED

## -MUTABLE OBJECTS:

```
-Definition: Objects whose state or value can be changed after creation are called mutable.
-Examples: Lists, dictionaries, and sets are common examples of mutable objects in Python.
-Characteristic: You can modify the content or structure of a mutable object. For example, you can add, remove, or change elements in a list.
```



## -TUPLE ARE IMMUTABLE
## -TUPLE CONTAIN IMMUTABLE OBJECT

```IMMUTABLE MEANING ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-Definition: Objects whose state or value cannot be changed after creation are called immutable.
-Examples: Integers, floats, strings, and tuples are examples of immutable objects in Python.
-Characteristic: Once an immutable object is created, you cannot modify its content or structure. Instead, if you want to change it, you create a  new object
-TUPLE PROCESSING IS FASTER THAN LIST
-TUPLE CONSUME LESS MEMORY
-ELEMENTS CAN BE ACCESED EASILY
```



# 2ND  WHAT IS DECORATOR
																										.
## -A FUNCTION THAT TAKE ANOTHER FUNCTION AS AN ARGUMENTAND THEN RETURN ANOTHER FUNCTION

```
-SYNTAX
def decoder_function(func):
	def wrapper_function():
		print(" Wraper function worked ")
		return func()
	print("decorator function worked ")
	return wrapper_function
def Show ():
	print("Show Worked")
decorator_function = decorator_function(Show)
decorator_show()

```

# 3RD  diffrence list and ddict comprehension

```
~LIST COMPREHENSION
~numbers = [1,2,3,4,5,6]
~even_nuber = [ x for x in numbers if x % 2 == 0]


~ DICT COMPREHENION
~numbers = [1,2,3,4,5,6]
~square_num =  {x: x**2 for x in numbers if x%2 == 0}

```
# 3RD DIFFRENCE BETWEEN GENERATOR AND ITERATOR

-GENARATOER
~~~ GENERATOR ARE ITERATOR WHICH ARE EXECUTE ONLY ONCE
~~~ GENERATOR USES (yield) keyword
~~~ GENERATORS ARE MOSTLY USED INLOOPS
~~~ EVERY GENERATOR IS AN ITERATOR
~~~~~~~~~   In Python, the next() function is used to retrieve the next item from an iterator. It takes two arguments:
~~~~~~~~~~~~EXAMPLE OF GENERATOR~~~~~~~~~~~~~~~
def sqr(n):
	for i in range(1,n+1):
		yield i*i
	a = sqr(3)
	print(next(a))
	print(next(a))
	print(next(a))

	output
	1
	4
	9

- ITERATOR
~~~ ITERSTOR IS AN OBJECT WHICH CONTAIN A COUNTABLE NUMBEER OF VALUES
~~~ IT IS USED TO ITERATE OVER ITERABLE OBJECTS
~~~LIKE LIST TUPLE SETS
~~~ITERATOR USES  [iter() and next()] FUNCTION
~~~EVERY ITERATOR IS NOT A GENERATOR




4TH WHAT IS INIT KEYWORD IN PYTHON

~~~~ [ |||||||||||||||||||||||||||||||||||||||||||||      __INIT__.PY {FILE}	       |||||||||||||||||||||||||||||||||||||||||||||||||||||||||| ]

~~~THIS FILE LET THE ITERPRETOR KNOW THAT A DIRECTORY CONTAINS CODE FOR A PYTHON MODULE
~~~ IT CAN BE BLANK
~~~WITHOUT ONE , YOU CANNOT IMPORT MODULES FROM ANOTHER FOLDER INTO YOUR PROJECT



||||||||||||||||||||||||||||||||||||||||||||||| THE ROLE ||||||||||||||||||||||||||||||||||||||||||||||||||

~~~ THE ROLE OF THE FILE IS SIMILAR TO THE FUNCTION IN PYTHON CLASS
~~~ IT SET UP HOW PACKAGES OR FUNCTIONS WILL BE IMPORTED INTO YOUR FILES


~~~~ [ |||||||||||||||||||||||||||||||||||||||||||||      __INIT__()FUNCTION	       |||||||||||||||||||||||||||||||||||||||||||||||||||||||||| ]


~~~ THE __INIT__ METHOD IS SIMILAR TO CONSTRUCTOR IN C++ AND JAVA
~~~ CONSTRUCTOR ARE USED RO INITIALIZE   THE OBJECT STATE


5TH DIFFRENCE BETWEEN MODULES AND


```
