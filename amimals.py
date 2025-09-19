# dog
# constructor - name,  breed
# method Bark - print "woof woof"

class Dog:
    def _init_(self,name, breed):
        self.name = name
        self.breed = breed

    
    def bark(self):
            print("woof woof")
  

class Cat:
    def _init_(self, name, breed):
          self.name =  name
          self.breed =  breed

    def meow(self):
        print("meow meow")      

    def printName(self):
        print(self.name)  
    def _str_(self):
        return "this class requires a name and breed \n method 1: print- meow meow, method 2: print-Kamsy"      


myDog = Dog("sierra","german shepherd")
myDog.bark()

myCat = Cat("skittles", "finx")
myCat.meow()
myCat.printName()


class Human:
    def _init_(self,name, eyes, nose, ears, skin,tongue,limbs,height):
        self.eyes = eyes
        self.nose = nose
        self.ears = ears
        self.skin = skin
        self.tongue = tongue
        self.limbs = limbs
        self.height = height 

        def walk(self):
            print(f{self.name}"I am walking.")

        def talk(self):
            print(f{self.name}"I am talking.")    

myHuman = Human("1","1","2","brown-skin","1","4","5.6ft")            


class Games:
    def _init_(self, sport_name, team_number, team_players):
        self.sport = sport_name
        self.team_number = team_number
        self.team_players = team_players_per_team

    def show(self):
        print(f{self.sport_name}"is my favourite to play") 
         print(f"We are "{self.team_number}"in my team") 
          print(f"There are"{self.team_players_per_team}"teams in total") 

football = Games("Football","11","2") 
basketball = Games("Basketball","6","2") 
Rugby = Games("Rugby","1","2") 
table_tennis = Games("Table Tennis","1","2")          

football.show()
basketballball.show()
rugby.show()
table_tennis.show()

