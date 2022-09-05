# Question a

class Student:
    
    def __init__(self,Name=None,ID=None,Institute=None):
        self.Name = Name
        self.ID = ID
        self.Institute = Institute
    
    def Display_info(self,):
        print("Name:",self.Name)
        print("ID:",self.ID)
        print("Institute’s Name:",self.Institute)
        
student_1 = Student("ABDULLAH AL MAMUN", 50238, "Manarat International University")
student_1.Display_info()

# Question b

class School_student(Student): 
    def __init__(self, Section, ResultSSC, DistrictOfSchool):
        super().__init__(self)
        self.Section = Section 
        self.ResultSSC = ResultSSC
        self.DistrictOfSchool = DistrictOfSchool  
          
    def Display_Info(self):
        print("Name:",self.Name)
        print("ID:",self.ID)
        print("Institute’s Name:",self.Institute)
        print("Section:",self.Section)
        print("Result(SSC):",self.ResultSSC)
        print("District of School:",self.DistrictOfSchool)


school_student = School_student("Science", "5.00", "Mymensingh")
school_student.Name = "ABDULLAH AL MAMUN"
school_student.ID = 50238
school_student.Institute = "Mawna ML High School"
school_student.Display_Info()

# Question c

class College_student(Student): 
    def __init__(self, Section, ResultPolytechnic, DistrictOfSchool):
        super().__init__(self)
        self.Section = Section 
        self.ResultPolytechnic = ResultPolytechnic
        self.DistrictOfSchool = DistrictOfSchool  
          
    def Display_Info(self):
        print("Name:",self.Name)
        print("ID:",self.ID)
        print("Institute’s Name:",self.Institute)
        print("Section:",self.Section)
        print("Result(Polytechnic):",self.ResultPolytechnic)
        print("District of School:",self.DistrictOfSchool)


student_college = School_student("Electrical", "3.58", "Dhaka")
student_college.Name = "ABDULLAH AL MAMUN"
student_college.ID = 50238
student_college.Institute = "Dhaka Polytechnic Institute"
student_college.Display_Info()

# Question d

class University_Student(Student):
    def __init__(self, Semester, CGPA):
        self.Semester = Semester
        self.CGPA = CGPA

    def Display_Info(self):
        print("Semester:",self.Semester)
        print("CGPA:",self.CGPA)

student_Unversity = University_Student("4th", "4.00")
student_Unversity.Display_Info()

# Question e

class Waiver(Student):
    def __init__(self):
        super().__init__(self)

    def Waiver_count(self):
        total = self.ResultSSC + self.ResultPolytechnic

        if total == 9:
            waiver = 100
        elif 8 <= total <= 8.99:
            waiver = 50
        elif 7 <= total <= 7.99:
            waiver = 25
        else:
            waiver = 0

        return waiver

    def Display_Info(self):
        print(f"Waiver: {self.Waiver_count()}%")

waiver_1 = Waiver()
waiver_1.ResultSSC = 5
waiver_1.ResultPolytechnic = 3
waiver_1.Display_Info()

# Question f

class Grade_Calculator(Student):
    def __init__(self, GPA1st, GPA2nd, GPA3rd):
        super().__init__(self)
        self.GPA1st = GPA1st
        self.GPA2nd = GPA2nd
        self.GPA3rd = GPA3rd

    def Count_CGPA(self):
        return (self.GPA1st + self.GPA2nd + self.GPA3rd)/3

    def Display_Info(self):
        print("ID:", self.ID)
        print(f"CGPA: {self.Count_CGPA():.2f}" )

grade_calculation = Grade_Calculator(4.00, 4.00, 4.00)
grade_calculation.ID = 5038
grade_calculation.Display_Info()

# Question g
# Assuming that ID is a very sensitive information

class Student:
     
    def __init__(self,Name=None, ID=None, Institute=None):       
        self.Name = Name
        self.Institute = Institute
        self.setID(ID)
    
    def Display_info(self,):
        print("Name:",self.Name)
        print("ID:",self.__ID)
        print("Institute’s Name:",self.Institute)

    def setID(self, ID):
        self.__ID = ID

    def getID(self):
        return self.__ID
        
student_1 = Student("ABDULLAH AL MAMUN", 50238, "Manarat International University")
student_1.Display_info()

class Grade_Calculator(Student):
    def __init__(self, GPA1st, GPA2nd, GPA3rd):
        super().__init__(self)
        self.GPA1st = GPA1st
        self.GPA2nd = GPA2nd
        self.GPA3rd = GPA3rd

    def Count_CGPA(self):
        return (self.GPA1st + self.GPA2nd + self.GPA3rd)/3

    def Display_Info(self):
        print("ID:", self.getID())
        print(f"CGPA: {self.Count_CGPA():.2f}" )

grade_calculation = Grade_Calculator(4.00, 4.00, 4.00)
grade_calculation.setID(50238)
grade_calculation.Display_Info()