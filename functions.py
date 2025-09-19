"""

"""

#def greetings():
#    print("Welcome to the application")

#greetings()

#def sum():
#    print("Enter your name:")
#    name = input()
#    print(f"My name is {name}")
    
#sum()    

#num1 = int(input("Enter your first number:"))
#num2 = int(input("Enter your second number:"))

#def add(a,b):
#    print(a + b)

#add(num1, num2)   

#bakeryList = ["bread", "cake","peanut","strawberry cake"]

#def  checkStock(pastry):
 #   counter = 0
  #  for item in pastry:
   #   if item != "strawberry cake":
    #      counter += 1
     #     print(counter, "loop")
      #    continue
      #else:
       #   print("Yes we are in stock")
#checkStock(bakeryList)


ClassList = ["justina", "victor","despina","somto", "kamsy",]    
def checkList(names):
    counter = 0
    for person in names:
        if person != "kamsy":
            counter += 1
            print("person", counter)
            continue
        else:
            if person == "kamsy":
                print("Yayy, that's me")    
checkList(ClassList);                