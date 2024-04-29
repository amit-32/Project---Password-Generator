import random
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m',
          'n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M',
          'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers=['0','1','2','3','4','5','6','7','8','9']

symbols=['!','#','$','&','%','(',')','*','+']

print("Welcome to Password Generator @@!!")

l=int(input("Enter How many Letters you want? \n"))
n=int(input("Enter How many Numbers you want? \n"))
s=int(input("Enter How many Symbols you want? \n"))

empty_list=[]
for i in range(1,(l+1)):
      p=random.choice(alphabet)     #it takes random alphabet
      empty_list +=p
for i in range(1,(n+1)):
      p=random.choice(numbers)      #it takes random number
      empty_list +=p
for i in range(1,(s+1)):
      p=random.choice(symbols)      #it takes random symbols
      empty_list +=p

random.shuffle(empty_list)          #it Shuffles the List
empty_str=""
for i in (empty_list):  
    empty_str +=i               #this for loop is used to put the elements
                                #of list into the string or to convert the list into string

print("Your Secured Password is:- ", empty_str)

