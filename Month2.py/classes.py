class User:
    First_Name ="Kamsy"
    Last_Nmae= "Mbah"
    Gender = "Female"
    Nationality = "Nigerian"
    Age = 30
    E_mail = "kamsimbah09@gmail.com"
    Phone_Number = "+2347049314020"

User1 = User()
User2 = User()

User1.First_Name = "Ifunaya"
print(User1.First_Name)

class User:
    def _init_(self, firstname, lastname, age, gender, nationality, email, phone):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.nationality = nationality
        self.email = email
        self.phone = phone

    def printFirstName(self):
        print(self.firstname)

    def printLastName(self):
        print(self.lastname)

    def printAge(self):
        print(self.age)

    def printGender(self):
        print(self.gender)
        
    def printNationality(self):
        print(self.nationality)

# object of the class User
user1 = User("Kamsy", "Mbah", 19, "Female", "Nigerian", "fake@gmail.com", "09060495111")
user1.printFirstName()


# user1.Lastname = "Okafor"
# print(user1.Lastname)
# print(user1.Firstname)
# print(user1.Lastname)
# print(user1.age)
# print(user1.Gender)
# print(user1.Nationality)
# print(user1.Email)
# print(user1.Phone)

