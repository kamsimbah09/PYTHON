# WHILE LOOP:

#start = 1
#end = 11
#while(start < 11):
  #  print(start)
   # start = start +1

# star = 13
# en = 36
# while(star < 36):
 #   print(star)
  #  star = star +1

#FOR LOOP:
mylist  = ["football", "basketball","tennis","golf","hunting","volleyball"]

counter = -1
for item in mylist:
    
    if item == "golf":
     print("yes this is golf")
     print(counter)
    else:
       counter += 1
       continue


num1 = int(input("Enter a number:"))
multiplier = 1
while (multiplier <= 12):
   print(num1 * multiplier)
   multiplier += 1


name = "Kamsy"
for letter in name:
   print(letter) 


for num in range(1, 10):
   print(num)