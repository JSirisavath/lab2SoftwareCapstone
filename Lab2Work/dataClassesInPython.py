from dataclasses import dataclass

# @dataclass is a decorator which has  presets given to you rather you typing in some methods implicitly, such as __init__, or __str__. Built in methods that is implicit as you use this decorator.


@dataclass
# Self is very similar to this keyword from Java
# Self refers to what is being pass inside the function to reference that variable is this class variable as well
# So 'This' object variable wil be equal to another variable that is being passed in as an argument. Essentially self is the object itself. In this case, this class name is equal to the passed in named
class Student:

    name: str  # Setting instance variable self to name

    # self (object it self) is equal to School id
    school_id: str

    gpa: float

    # Override and customize strings output. Can leave this out for decorator, but for traditional version that handles other logic, need to specify __str__ method
    def __str__(self):
        return f'Name: {self.name}, GPA: {self.gpa}, StudentId: {self.school_id}'


def main():
    # Student objects examples
    Jay = Student('Jay', 'fc2985up', 3.69)

    print(Jay)

    Alex = Student('Alex', 'fdsfewrw34', 3.39)

    print(Alex)

    Bill = Student('Bill', 'fadsf343432', 3.99)

    print(Bill)


if __name__ == '__main__':
    main()
