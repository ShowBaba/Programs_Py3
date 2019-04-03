score_list = []
print("How many students are there? ")
num_stud = int(input(":"))

print("Input a score then enter to input the next")

for stud_score in range(num_stud):
    stud_score = int(input(":"))
    score_list.append(stud_score)
    
for scores in score_list:
    if scores >= 70 and scores <= 100:
        print("A")
    elif scores >= 60 and scores <= 69:
        print("B")
    elif scores >= 50 and scores <= 59:
        print("C")
    elif scores >= 45 and scores <= 49:
        print("D")
    else:
        print("F")
        
