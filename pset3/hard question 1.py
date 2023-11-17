LETTER_GRADES = {
     "A+": 4.0,
     "A": 4.0,
     "A-": 3.7,
     "B+": 3.3,
     "B": 3.0,
     "B-": 2.7,
     "C+": 2.3,
     "C": 2.0,
     "C-": 1.7,
     "D+": 1.3,
     "D": 1.0,
     "F": 0
}
grades = []
flag = True
grade_point_avg = 0

def gpa(grades):
     sum = 0

     for i in grades:
          sum += LETTER_GRADES[i.upper()]
     
     mean = sum/len(grades)

     return mean

while flag:
     grade = input("Enter a grade. Enter nothing to finish. \n")

     if grade == "":
          grade_point_avg = gpa(grades)
          formatted = format(grade_point_avg, ".2f")
          print(f"GPA is {formatted}")
          flag = False
     else:
          grades.append(grade)
