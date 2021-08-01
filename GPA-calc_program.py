credits_array = []
no_of_subs = int(input("Enter number of subjects : "))
sum_of_credits = 0

for i in range(0, no_of_subs):
    credits = float(input("Enter your credits for each sub:"))
    credits_array.append(credits)
print("The credits are : ", credits_array)
sum_of_credits = sum(credits_array)
print("The sum of credits is : ", sum_of_credits)
print("----------END OF CREDITS----------")
sub_grade_array = []
for i in range(0, no_of_subs):
    grade_in_sub = float(input("Enter grade in each subject : "))
    sub_grade_array.append(grade_in_sub)
print("The subject grades are : ", sub_grade_array)
print("----------END OF SUBJECTS----------")
grade_points = []
for i in range(0, no_of_subs):
    grade_points.append(credits_array[i] * sub_grade_array[i])
print(grade_points)
sum_grade_points = 0
i = 0
while i < len(grade_points):
    sum_grade_points = sum_grade_points + grade_points[i]
    i += 1
print(sum_grade_points)
gpa = sum_grade_points/sum_of_credits
print(gpa)
