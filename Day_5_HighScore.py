student_scores = input("input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

higest_score = 0
for higher_score in range(0,len(student_scores)):
    if student_scores[higher_score] > higest_score:
        higest_score = student_scores[higher_score]
        print(higest_score)


print(higest_score," is the higest score of the group")

