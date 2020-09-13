def getGradePoint(grade):
  if grade == "A":
    gradepoint = 4
  elif grade =="A-":
    gradepoint = 3.67
  elif grade == "B+":
    gradepoint = 3.33
  elif grade == "B":
    gradepoint = 3
  elif grade == "B-":
    gradepoint = 2.67
  elif grade == "C+":
    gradepoint = 2,33
  elif grade == "C":
    gradepoint = 2
  elif grade == "D":
    gradepoint = 1
  else :
    gradepoint = 0
  return gradepoint

  

 
if __name__ == "__main__":
 gradepoint=0
 credit=0
 for i in range(1,4):
   grade = input(f"Enter your course {i} letter grade: " )
   coursecredit = input(f"Enter your course {i} credit: ")
   coursecredit = int(coursecredit)
   gradepoint += getGradePoint(grade)*coursecredit
   credit += coursecredit
   print(f"Grade point for course {i} is: {getGradePoint(grade)}")
   print(f"Your GPA is: {gradepoint/credit}")