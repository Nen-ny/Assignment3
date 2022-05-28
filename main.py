class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):

        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    
    def change_name(self):
        print("Favour")
    
    def change_age(self):
        print("20")

    def add_track(self):
        print("Full Stack")
    
    def get_score(self):
        print("12.698")
    
        pass
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name()
Bob.change_age()
Bob.add_track()
Bob.get_score()
