# number= [1,2,3]
# new_numbers = [n + 1 for n in number]
# print(new_numbers)
# even_list = [num * 2 for num in range(1,10)]
# print(even_list)
# names = ["alexa", "siddique", "sohil", "sammeer", "vamsi"]
# short_names = [name for name in names if len(name) < 6]
# print(short_names)
# long_names = [name.upper() for name in names if len(name) > 6]
# print(long_names)
# numbers = [1,2,3,4,5,66,77,88,99,100]
# squared_num = [num * num for num in numbers]
# print(squared_num)

# import random
# students  = ["alexa", "siddique", "sohil", "sammeer", "vamsi"]
# students_score = {students:random.randint(1,100) for students in students}
# #[key:value for (key,value) for in test]
# passed_students = {students:score for(students,score) in students_score.items()if score >= 36}
# print(passed_students)

student_dict = {
    "students":["alexa", "siddique", "sohil", "sammeer", "vamsi"],
    "score":[50,90,80,60,95]
}
# for (key,values) in student_dict.items():
#     print(values)
import pandas 
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index,row) in student_data_frame.iterrows():
    print(row.score)
    
















