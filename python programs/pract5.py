class Student:
    def __init__(self,name,rollno,score):
     self.name=name
     self.rollno=rollno
     self.score=score

    def gradecalculate(self):
        if(self.score>=80 and self.score<=100):
             grade="A"
        elif(self.score>=60 and self.score<80):
             grade="B"

        elif(self.score>=50 and self.score<60):
             grade="C"
        elif (self.score >=0 and self.score < 50):
             grade = "F"
        else:
             print(" Invalid score ")
        print("Student name : ",self.name,"\nRollNo : ",self.rollno,"\nGrade",grade)




student1=Student("Orvell",8671,85)
student1.gradecalculate()