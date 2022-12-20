
                                                                    # HW 13

class Human:
    def __init__(self, name: str, surname: str, age: int, phone: str, adress: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.adress = adress

    def get_info(self):
        print(f'{self.name}, {self.surname}, {self.age}, {self.phone}, {self.adress}')
        pass

    def call(self):
        print(f'{self.phone}')
        pass


victor = Human('Victor', 'Popov', 31, '+38 067 961 08 45', 'm.Kharkiv, Sumska str. 12, app 14')
olha = Human('Olha', 'Volk', 24, '+38 099 123 88 99', 'm.Zaporizsha, Stepana Bendery str. 118')
alexey = Human('Alexey', 'Nosin', 44, '+38 063 236 47 58', 'm.Lviv, Striyska str. 53, app 236')


victor.get_info()
olha.get_info()
alexey.get_info()

victor.call()


