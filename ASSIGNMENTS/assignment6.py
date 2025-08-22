"""
This program prints out numbers 1 to 30
"""

star = 1
while(star < 31):
  if(star %3 == 0):
    print("fizz")
  elif(star % 5 == 0):
    print("buzz") 
  else:
    print(star)
  star += 1       