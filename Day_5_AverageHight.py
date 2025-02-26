student_heights = input("input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

sum_heights =  0

for i in range(0,len(student_heights)):
    sum_heights += student_heights[i]

print(sum_heights)

avrage_height = sum_heights/len(student_heights)

print(round(avrage_height))
