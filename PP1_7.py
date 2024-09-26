'''
  Lesson: Booleans
  Author: Helen Lin
  Date Created: September 25, 2024
  Date Last Modified: September 25, 2024
'''

def q1():
  #Write code here
  bool1 = True
  print(bool1)

def q2():
  #Write code here
  num1 = input("Input an integer: ")
  num1 = int(num1)
  bool1 = True
  bool1 = False
  bool1 = 5 >= num1
  print(bool1)

def q3():
  #Write code here
  bum = input("Input the letter a: ")
  bool1 = True
  bool1 = False
  bool1= bum == "a"
  print(bool1)

def q4():
  #Write code here
  word = input("Input a word that comes earlier than the word google: ")
  bool1 = True
  bool1 = False
  bool1 = "google" > word
  print(bool1)

def q5():
  #Write code here
  num1 = input("Input an integer: ")
  num2 = input("Input another integer: ")
  num1 = int(num1)
  num2 = int(num2)
  bool1 = True
  bool1 = False
  bool1 = num1*num2 >= 40 
  print(bool1)

#Do edit the code below
#Comment the lines below when running your tests

q1()
q2()
q3()
q4()
q5()
