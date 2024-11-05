'''
  Lesson: Booleans
  Author: Helen Lin
  Date Created: September 25, 2024
  Date Last Modified: September 25, 2024
'''

def q1():
  #Write code here
  bool = True
  print(bool)

def q2():
  #Write code here
  num1 = input("Input an integer: ")
  num1 = int(num1)
  bool = 5 >= num1
  print(bool)

def q3():
  #Write code here
  bum = input("Input the letter a: ")
  bool = bum == "a"
  print(bool)

def q4():
  #Write code here
  word = input("Input a word that comes earlier than the word google: ")
  bool = "google" > word
  print(bool)

def q5():
  #Write code here
  num1 = input("Input an integer: ")
  num2 = input("Input another integer: ")
  num1 = int(num1)
  num2 = int(num2)
  bool = num1*num2 >= 40 
  print("Your numbers multiplied together are greater than 40:")
  print(bool)

#Do edit the code below
#Comment the lines below when running your tests

#q1()
#q2()
#q3()
#q4()
#q5()
