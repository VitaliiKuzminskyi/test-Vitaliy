
                                                                    # HW 13


users = [
    {
        'name': 'Victor',
        'surname':'Popov',
        'age': 31,
        'phone':'+38 067 961 08 45',
        'adress': 'm.Kharkiv, Sumska str. 12, app 14'
    },
    {
        'name': 'Olha',
        'surname':'Volk',
        'age': 24,
        'phone':'+38 099 123 88 99',
        'adress': 'm.Zaporizsha, Stepana Bendery str. 118'
    },
    {
        'name': 'Alexey',
        'surname':'Nosin',
        'age': 44,
        'phone':'+38 063 236 47 58',
        'adress': 'm.Lviv, Striyska str. 53, app 236'
    }
]

print()
class Human:
    def __init__(self, name: str, surname: str, age: int, phone: str, adress: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.adress = adress

    def get_info(self):
        # print(f'{self.name}, {self.surname}, {self.age}, {self.phone}, {self.adress}')
        # print(users)
        users_d()
        pass

    def call(self):
        print(f'{self.phone}')
        pass





# for user in users:
#     # print(user['name'], user['surname'], user['age'], user['phone'], user['adress'])
#     print(user)



victor = Human('Victor', 'Popov', 31, '+38 067 961 08 45', 'm.Kharkiv, Sumska str. 12, app 14')
# olha = Human('Olha', 'Volk', 24, '+38 099 123 88 99', 'm.Zaporizsha, Stepana Bendery str. 118')
# alexey = Human('Alexey', 'Nosin', 44, '+38 063 236 47 58', 'm.Lviv, Striyska str. 53, app 236')
#
# #
victor.get_info()
# olha.get_info()
# alexey.get_info()
# #
# victor.call()



