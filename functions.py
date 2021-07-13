Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f=open("C:/Users/Vaishnavi/Desktop/hello.txt")
>>> f.read()
'Hello, I am Vaishnavi Managoli.My favourite color is lavender or green.\nMy age is 13.I am in 8th class.'
>>> f=open("C:/Users/Vaishnavi/Desktop/hello.txt")
>>> file=f.readlines()
>>> for i in file:
	print (i)

	
Hello, I am Vaishnavi Managoli.My favourite color is lavender or green.

My age is 13.I am in 8th class.
>>> sentence= "I am Vaishnavi Managoli. I live in India."
>>> words=sentence.split
>>> 
>>> words=sentence.split()
>>> print(words)
['I', 'am', 'Vaishnavi', 'Managoli.', 'I', 'live', 'in', 'India.']
>>> sentence="I am Vaishnavi Managoli. I live in India
SyntaxError: EOL while scanning string literal
>>> sentence="I am Vaishnavi Managoli. I live in India"
>>> words=sentence.split(".")
>>> print(words)
['I am Vaishnavi Managoli', ' I live in India']
>>> def greet(name):
	print("hello" + name)

	
>>> greet("Vaishnavi")
helloVaishnavi
>>> def countwordsFromFile():
	fileName=input("Enter the file name:-")
	numberOfWords=0
	file=open(fileName,'r')
	for i in file:
		words=line.split()
		numberOfWords=numberOfWords+ len(words)
	print("Number of words are:-")
	print(numberOfWords)

	
>>> countwordsFromFile()
Enter the file name:- hello1.txt
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    countwordsFromFile()
  File "<pyshell#28>", line 4, in countwordsFromFile
    file=open(fileName,'r')
FileNotFoundError: [Errno 2] No such file or directory: ' hello1.txt'
>>> countwordsFromFile()
Enter the file name:-C:/Users/Vaishnavi/Desktop/hello.txt
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    countwordsFromFile()
  File "<pyshell#28>", line 6, in countwordsFromFile
    words=line.split()
NameError: name 'line' is not defined
>>> def countwordsFromFile():
	fileName=input("Enter the file name:-")
	numberOfWords=0
	file=open(fileName,'r')
	for i in file:
		words=i.split()
		numberOfWords=numberOfWords+ len(words)
	print("Number of words are:-")
	print(numberOfWords)

	
>>> countwordsFromFile()
Enter the file name:-C:/Users/Vaishnavi/Desktop/hello.txt
Number of words are:-
21
>>> 