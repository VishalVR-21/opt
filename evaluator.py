# def evaluate(input_file_name, output_file_name):
#     fin = open(input_file_name, 'r')
#     fout = open(output_file_name, 'r')

#     try:
#         points = 0

#         # Write the evaluation code here.
#         # Read the input from fin file object
#         # Read the output from fout file object

#     except Exception as e:
#         fin.close()
#         fout.close()

#         return {'result': 'WA', 'error': str(e), 'points': 0}

#     fin.close()
#     fout.close()

#     return {'result': 'AC', 'points': points}
def evaluate(input_file_name, output_file_name):
    fin = open(input_file_name, 'r')
    fout = open(output_file_name, 'r')

    try:
        skill_set_list = []
        question_skill_set_list = set([])
        k = 0
        with open(input_file_name, 'r') as f:
            k = int(f.readline())
            for j in range(k):
                m = int(f.readline())
                line = f.readline().strip()
                question_skill_set = question_skill_set.union(
                    set(line.split()))
                question_skill_set_list.append(question_skill_set)
                n = int(f.readline())
                skill_set = {}
                for i in range(n):
                    line2 = f.readline().strip()
                    m = int(line2.split()[0])
                    line = f.readline().strip()
                    skills = line.split()
                    skill_set[m] = skills
                skill_set_list.append(skill_set)
        points = 0
        with open(output_file_name, 'r') as f:
            for i in range(k):
                n = int(f.readline())
                for j in range(n):
                    line = f.readline().strip()
                    ids = line.split()
                    team_skills = set([])
                    for l in ids:
                        for skills in skill_set_list[i][l]:
                            team_skills.add(skills)
                    if question_skill_set_list[i].issubset(team_skills):
                        points += 1
        fin.close()
        fout.close()
        return {'result': 'AC', 'points': points}
    except Exception as e:
        fin.close()
        fout.close()
        return {'result': 'WA', 'error': str(e), 'points': 0}


# def evaluate(input_file_name, output_file_name):
#     fin = open(input_file_name, 'r')
#     fout = open(output_file_name, 'r')

#     try:
#         skill_set = {}
#         question_skill_set = set([])
#         with open(input_file_name, 'r') as f:
#             t = int(f.readline())
#             for j in range(t):
#                 m = int(f.readline())
#                 line = f.readline().strip()
#                 question_skill_set = question_skill_set.union(
#                     set(line.split()))
#                 n = int(f.readline())
#                 for i in range(n):
#                     line2 = f.readline().strip()
#                     m = int(line2.split()[0])
#                     line = f.readline().strip()
#                     skills = line.split()
#                     skill_set[m] = skills
#         points = 0
#         with open(output_file_name, 'r') as f:
#             n = int(f.readline())
#             total_teams = []
#             for i in range(n):
#                 team = []
#                 line = f.readline().strip()
#                 team.append(line)
#                 total_teams.append(team)
#             for each_team in total_teams:
#                 team_skills = set([])
#                 for member in each_team:
#                     for skills in skill_set[member]:
#                         team_skills.add(skills)
#                 if question_skill_set.issubset(team_skills):
#                     points += 1

#         return {'result': 'AC', 'points': points}

#     except Exception as e:
#         fin.close()
#         fout.close()
#         return {'result': 'WA', 'error': str(e), 'points': 0}

#     fin.close()
#     fout.close()
