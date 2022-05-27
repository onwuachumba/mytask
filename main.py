from unicodedata import name


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age:int,tracks,score):
        self.tracks=['track1','track2',"track3"]
        self.name = name
        self.age = age
        self.track = tracks[0]
        self.score = score
    def change_name(self,new_name):
        self.name = new_name    
    def change_age(self,new_age:int):
        self.age = new_age    
    def add_track(self,new_track):
        self.tracks.append(new_track)
    def get_score(self):
        return self.score
        


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("paul")
Bob.change_age(29)
Bob.add_track("UI/UX")
Bob.get_score()
print(Bob.name)
print(Bob.tracks)
print(Bob.score)
print(Bob.age)
print(Bob.age)