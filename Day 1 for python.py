Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5+5
10
>>> name = "Ishita"
>>> print(name)
Ishita
>>> age = "twelve"
>>> print(name)
Ishita
>>> print(age)
twelve
>>> age = 12
>>> print(age)
12
>>> myfriends = ["reet", "anadhya", "]
	     
SyntaxError: EOL while scanning string literal
>>>  myfriends = ["reet", "anadhya", "sneha", "shreya"]
 
SyntaxError: unexpected indent
>>> my friends = ["reet", "anadhya", "sneha", "shreya"]
SyntaxError: invalid syntax
>>> myfriends = ["reet","anadhya","sneha","shreya"]
>>> print(myfriends)
['reet', 'anadhya', 'sneha', 'shreya']
>>> print(sneha)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(sneha)
NameError: name 'sneha' is not defined
>>> print(2)
2
>>> print(myfriends[2])
sneha
>>> print(myfriends[0])
reet
>>> print(myfriends[1])
anadhya
>>> print(myfriends[3])
shreya
>>> day = input("What is the day today?")
What is the day today?
>>> day = input("What is the day today?")
What is the day today? tuesday
>>> 555+111
666
>>> number1= input("Enter number 1")
Enter number 1 1123
>>> number2= input("Enter number 2")
Enter number 2 3456
>>> number1 + number2
' 1123 3456'
>>>   age = input("Is he/she above is 18?")
  
SyntaxError: unexpected indent
>>> for i in range(0,15):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
>>> name = "Ishita Bansal"
>>> count = 0
>>> for i in range(0,len(name)):
	if(name[i]!=' '):
		count = count+1

		
>>> print("total characters are? "+)
SyntaxError: invalid syntax
>>> name = "Ishita Bansal"
>>> count = 0
>>> for i in range(0,len(name)):
	if(name[i]!=' '):
		count = count+1

		
>>> print("total characters are? "+str(count))
total characters are? 12
>>> 