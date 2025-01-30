from datetime import date


class Person:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        national_code: int,
        birth_date: date,
        location: str = "Esfahan",
    ):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.national_code: int = national_code
        self.birth_date: date = birth_date
        self.location: str = location
        self.__password: str

    def get_fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, new_password: str) -> bool:
        result: bool = False
        if len(new_password) < 6:
            print("password should have at least 6 characters")
        else:
            self.__password = "hjfhjJB3J5H" + new_password + "36aergeakjhfk"
            result = True
        return result


class Student(Person):
    total_students: int = 0

    def __init__(
        self,
        first_name: str,
        last_name: str,
        national_code: int,
        birth_date: date,
        major: str,
        gpa: float,
    ):
        super().__init__(
            first_name=first_name,
            last_name=last_name,
            national_code=national_code,
            birth_date=birth_date,
        )
        self.major: str = major
        self.gpa: float = gpa
        Student.total_students += 1

    def get_status(self):
        if self.gpa <= 16:
            print("he/she more practicing")
        elif 16 < self.gpa <= 17:
            print("she/he is ok")
        else:
            print("she/he is outstanding")

    def get_fullname(self) -> str:
        return f"{self.first_name} {self.last_name} | {self.major}"

    @staticmethod
    def get_total_students_number() -> int:
        return Student.total_students


birth_date = date(1991, 5, 25)
s1 = Student(
    first_name="Peyman",
    last_name="Barjoueian",
    national_code=123455678,
    birth_date=birth_date,
    major="Computer",
    gpa=17.5,
)
print(s1.get_fullname())
s1.get_status()


s2 = Student(
    first_name="Golnaz",
    last_name="Akbari",
    national_code=245634647,
    birth_date=birth_date,
    major="Mechanic",
    gpa=19,
)

print(s2.get_fullname())
s2.get_status()

print(Student.get_total_students_number())
