class Person:
    def __init__(self, name_param, age_param):
        self.name = name_param
        self.age = age_param
        print("hihi i am created", self, self.name, self.age)

    def talk(self):
        print("안녕하세요 저는", self.name, "이고 나이는", self.age, "살입니다.")


person_1 = Person("Ronaldo", 36)
person_1.talk()

person_2 = Person("Faker", 29)
person_2.talk()
