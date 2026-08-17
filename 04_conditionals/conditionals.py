# Python Conditional Statements

age = 21
if age >=18:
  print("You are an adult.")
else:
  print("You are not an adult.") 

---

# if, Elif , Else

marks = 75

if marks >= 90:
  print("Grade A+")
elif marks >= 75:
  print("Grade A")
elif marks >= 60:
  print("Grade B")
else:
  print("Grade C")


---

# Student Result

attendance = 85

if attendence >= 75:
  print("Eligible for exam")
else:
  print("Not eligible for exam")


if -> first condition
elif -> another condition if the previous one was false
else -> everything above was false

---

#combined conditions

cgpa = 8.5
internship = False

if cgpa >= 8.0 and not internship:
  print ("Apply now")
else:
  print ("Wait")
