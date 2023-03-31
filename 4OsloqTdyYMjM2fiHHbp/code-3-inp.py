# # n number of students
# # student id
# # list of skills
# # list contain the topic that we need
# import itertools
# import random,string
# import random
#
# # Define the range of input values
# MIN_SKILLS = 1
# MAX_SKILLS = 3
# MIN_STUDENTS = 5
# MAX_STUDENTS = 10
# MIN_SKILLS_PER_STUDENT = 1
# MAX_SKILLS_PER_STUDENT = 3
#
# # Generate random input
# n_skills = random.randint(MIN_SKILLS, MAX_SKILLS)
# skills = [f'skill_{i}' for i in range(1, n_skills+1)]
# n_students = random.randint(MIN_STUDENTS, MAX_STUDENTS)
# problem_skills = set(random.sample(skills, random.randint(1, n_skills)))
# students = []
# for i in range(1, n_students+1):
#     student_skills = random.sample(skills, random.randint(MIN_SKILLS_PER_STUDENT, MAX_SKILLS_PER_STUDENT))
#     students.append((i, student_skills))
#
# # Print output
# print(n_skills)
# print(' '.join(skills))
# print(n_students)
# for student in students:
#     print(f"{student[0]} {len(student[1])} {' '.join(student[1])}")
#
#
# # 2
# # skill_1 skill_2
# # 5
# # 1 1
# # skill_2
# # 2 2
# # skill_1 skill_2
# # 3 2
# # skill_1 skill_2
# # 4 1
# # skill_1
# # 5 1
# # skill_2
# # i = int(input("enter the number"))
# # k = int(input("enter the skills for question"))
# # question = input().split(' ')
# # temp = question
# # number = int(input("enter the number of student"))
# # g = 0
# # m = {}
# # for g in range(number):
# #     k = int(input("enter the number student_id"))
# #     b = int(input("enter the number of skills"))
# #
# #     skills = input().split(' ')
# #     m[g] = skills
# # count = 0
# # print(len(question))
# # print("outputs")
# # for ans in question:
# #     for i in m.values():
# #         for j in i:
# #             if ans == j:
# #                 print(ans,j)
# #                 print(len(question))
# #                 if len(question) == 0:
# #                     count += 1
# #                     question = temp
# #                 else:
# #                     if ans in question:
# #                         question.remove(ans)
# #
# # print(count)
#
# '''1
# 9
# UUHX DSKX BMHL USKU ZGCVYQ TUVQOLD RINBG GSAVGMQ JXFNR
# 10
# 1
# 6
# GCHBLL OAZS RINBG BMHL TUVQOLD DSKX
# 2
# 4
# PHPZTAG JJFED GSAVGMQ UMFF
# 3
# 5
# KLBFO HUPF ZGCVYQ BMHL USKU
# 4
# 5
# VLPT XYRO LMLMJ JXFNR GSAVGMQ
# 5
# 4
# XUQBNAG SMKLZTE CBIH DSKX
# 6
# 4
# CNGKNW ZJFC VUBNQQ UUHX
# 7
# 4
# TUVQOLD PUKIU FMKDWXR DDBJ
# 8
# 4
# BDQJS RINBG ZGCVYQ DSKX
# 9
# 4
# NBOJB BIBUJ EEHWIG JXFNR
# 10
# 6
# YEMAR DACA UGSVU   RINBG  
# '''
#
# import itertools
#
# with open('test1.txt') as f:
#
#     test_case = int(f.readline())
#     case = int(f.readline())
#     print(case)
#     for _ in range(test_case):
#         n_skills = int(f.readline())
#         l = []
#         skills = {f.readline()}
#         print(skills)
#         n_students = int(f.readline())
#
#         problem_skills = set(skills)
#
#         students = {}
#         for i in range(n_students):
#             student_id, n_skills = map(int, f.readline().split(' '))
#             student_skills = {f.readline()}
#             students[student_id] = student_skills
#
#     # Initialize list of teams
#         teams = []
#
#     # Create all possible combinations of teams
#         for i in range(1, 4):
#             for team in itertools.combinations(students.keys(), i):
#             # Create set of skills studied by the team
#                 team_skills = set()
#                 for student_id in team:
#                     team_skills.update(students[student_id])
#
#             # Check if the team has all the skills required to solve the problem
#                 if problem_skills.issubset(team_skills):
#                     teams.append(team)
#
#     # Find maximum number of teams that can solve the problem
#         max_teams = 0
#         for i in range(1, 4):
#             n_teams = len([team for team in teams if len(team) == i])
#             if n_teams > 0:
#                 max_teams += 1
#
# # Print output
#     print(max_teams)
#
#
# # 4
# # python java c++ sql
# # 5
# # 1 2 python c++
# # 2 2 c++ sql
# # 3 3 python java sql
# # 4 2 java sql
# # 5 1 java
import excel2json
print("hello world")