number = int(input("Student Score: "))

if number >= 70 and number <= 100:
    print("Grade = A")
elif number >= 60 and number <= 69:
    print("Grade = B")
elif number >= 50 and number <= 59:
    print("Grade = C")
elif number >= 45 and number <= 49:
    print("Grade = D")
else:
    print("Grade = F")
