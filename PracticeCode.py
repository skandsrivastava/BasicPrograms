#print("Skand")

###########################

#def add_number(num1, num2):
  #return num1 + num2

#result = add_number(2,8)

#print(result)

#############################

#A= int ( input("Enter The Basic Salary :"))
#B= int ( input( "Enter The Amount Of Saving Done During The Month :"))

#if A <= 50000:
 # TT =0

#elif A <= 80000:
#  if B <= 50000:
#    TS = A - B
#    TT = TS * 0.05

#elif A <= 100000:
#  if B <= 70000:
#    TS = A - B
#    TT = TS * 0.10

#else:

#  if B <= 100000:
#    TS = A - B
#    TT = TS * 0.19

#print ("THE AMOUNT LEFT AFTER SAVING IS :",TS) 
#print ("THE TAX YOU HAVE TO PAY AT LAST IS :",TT)
#print ("$")
#print ("$")
#print ("YOU ARE A RESPONSIBLE CITIZEN OF INDIAN")

#################################

""" FOR LOOP PROGRAM:::::::::::::"""

#A = range (10)
#print (A)

#for i in range (10):
 # print (i)

#for i in range (100000):
 # print (i**3)




"""WAP to generate the table of a no ask by a user?"""
#Table = int ( input ("ENTER A NO WHICH TABLE YOU WANT :")) 
#for i in range (1,11) :
#  print(Table,"X",i,"=",Table*i)




"""WAP to print cubes of number in a range?"""
#a = int ( input("ENTER THE FIRST NO OF THE RANGE FOR WHICH YOU WANT A CUBE OF A NUMBER: "))
#b = int ( input("ENTER THE SECOND NO OF THE RANGE FOR WHICH YOU WANT A CUBE OF A NUMBER: "))
#c = b + 1
#for i in range (a , c):
#  print ("CUBES OF A NUMBER'S",i,"is:",i**3)



"""WAP to print a square ROOT of every alternate number in a range?"""
#a = int ( input("ENTER THE FIRST NO OF THE RANGE FOR WHICH YOU WANT A SQUARE ROOT OF AN ALTERNATE NUMBER: "))
#b = int ( input("ENTER THE SECOND NO OF THE RANGE FOR WHICH YOU WANT A SQUARE ROOT OF AN ALTERNATE NUMBER: "))
#c = b + 1 
#for i in range (a , c , 2):
#  print ("SQUARE OF",i,"is :",i**0.5)



########  WHILE LOOP PPROGRAM :::::::::::::::::::



"""WAP TO CALCULATE THE PRODUCTS OF TWO INPUTTED INTEGERS WITHOUT USING * OPERATOR; INSTEAD USING REPEATED ADDITION?"""
#a = int ( input ("Enter first no :"))
#b = int ( input ( "Enter the second no :"))
#p = 0
#c = a

#while c > 0:
#    c = c - 1
#    p = p + b

#print ("Product Of Two No",a,"and",b,"is:",p ) 





"""WAP TO CALCULATE FACTORIAL OF A NUMBER USING WHILE LOOP"""
#a = int ( input ("ENTER THE NO THAT HAS TO BE FACTORIAL :"))
#fact = 1
#term = a
#while a > 0:
#  fact = fact * a
#  a = a - 1

#print ("THE FACTORIAL OF",term,"IS :",fact )




"""WAP TO CALCULATE THE TOTAL AMOUNT PAYABLE BY THE COSTOMER ON PURCHASE ON ANY ITEM ON GST LEVIED ON IT. 
 DEVELOP A USER - FRIENDLY APPROACH FOR THE PROGRAM USING WHILE LOOP"""

#a = 'bill'

#tap = 0

#while a == 'bill' or a == 'BILL' or a == 'Bill':
#  ta = int ( input ("ENTER THE TOTAL AMOUNT OF THE ITEM :"))
#  gst = int (input ("ENTER THE GST ON THE ITEM :"))
#  a = input("Enter 'BILL' IF more item to be calculate OR Else press any key :")
#  tap = tap + (ta + (ta * gst) / 100)
  

#print ("THE AMOUNT TO BE PAY AFTER THE GST IS",tap)
#print ("THANKS   FOR   USING")



"WAP TO PRINT NATURAL NO USING WHILE LOOP"

#a = 0 
#b = int (input ("ENTER THE LAST DIGIT OF THE NATURAL NO :"))


#while a <= b:
#  print ("THE NATURAL NO ARE : ",a)
#  a += 1  


"WAP TO ACCEPT NO FROM THE USER AND CLACULATE THE SUM OF ALL THE NO BETWEEN ALL NO FROM 1 TO THE GIVEN NO ?"

#a = int ( input ("ENTER THE NO OF YOUR CHOICE WHICH YOU WANT TO HAVE A SUM :"))
#b = a + 1
#c = 0
#for i in range ( 1 , b , 1):
#  c = c + i
#print ("sum is :",c)  






"WAP TO PRINT THE PATTERN"
b = int (input ( "ENTER EITHER 1 OR 2 OF YOUR OWN CHOICE TO SEE THE MAGIC : "))
print ("NICE CHOICE ONE STEP AWAY FROM MAGIC")
a = int ( input ( "ENTER THE NO OF ROWS YOU WANTED TO PRINT TO GET A MAGIC : ")) 
if b == 1:
 for i in range ( 0 , a ):
  for j in range ( 0 , a - i - 1 ):
    print (end = " ")
  for j in range ( 0 , i + 1 ):
    print ( "*", end = " ")
  print () 
elif b == 2 :
 for i in range (1 , a + 1):
  for j in range (1 , i + 1):
    print (j , end=" " )
  print ( )
else:
  for i in range (6):
    for j in range ( 7 ):
      if (i == 0 and j %3!= 0) or (i == 1 and j %3 == 0) or (i - j == 2) or (i + j == 8):
        print ( "*" , end= " ")
      else:
        print (end = " " )  
    print ( )
  print ("NEXT TIME ATTEMP THE RIGHT CHOICE BETWEEN 1 AND 2")  
print ("HOPE YOU LIKE THE MAGIC") 

    










######## STRINGS ..................................