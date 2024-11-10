"""
All about mankind
"""

class Human:
    def __init__(self, height, weight, gender):
        self.height = height
        self.weight = weight
        self.gender = gender
#inheritance
class Police(Human):
    def __init__(self, height, weight,gender,nationality, cases):
        super().__init__(height, weight,gender)
        self.nationality = nationality
        self.cases = cases




class cs_student(Human):
    def __init__(self, height, weight, gender, is_love_coding):
        super().__init__(height, weight,gender)
        self.is_love_coding = is_love_coding

if __name__ == "__main__":

    police = Police(6,70,"male","Bangladeshi", False)
    print(police.nationality)     

    programmer = cs_student(5.5, 60, "female", True)     

    print(programmer.gender)