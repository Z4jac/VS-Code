import datetime
"""
class User:
    pass

user1 = User()
user1.first_name = "Dave"
user1.last_name = "Smith"
user1.age = 37

print(user1.first_name, user1.last_name)

user2 = User()
user2.first_name = "John"
user2.last_name = "Smith"
user2.book = "book"

print(user2.first_name, user2.last_name)
"""

class User:
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday #yyyymmdd

        #extract first and last name
        name_pieces = full_name.split(' ')
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]


    def age(self):
        """reurn the age of the user in years"""
        today = datetime.date(2001, 5, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd) #date of birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)

user = User("Dave Bowman", "19710315")
print(user.age())
