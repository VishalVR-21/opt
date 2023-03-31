def evaluate(input_file_name, output_file_name):
    fin = open(input_file_name, 'r')
    fout = open(output_file_name, 'r')

    try:
        with open('test1.txt', 'r') as f:
            input_str = f.read().strip()

    # Read the output file
        with open('output.txt', 'r') as f:
            output_str = f.read().strip()
        input_lines = input_str.split('\n')
    problem_skills = set(input_lines[1].split())
    n_students = int(input_lines[2])
    student_skills = []
    for line in input_lines[3:]:
        student_id, n_skills, *skills = line.split()
        student_skills.append(set(skills))

    # Parse the output
    n_teams = int(output_str[2])

    # Compute the score
    team_skills = [set.union(*skills) for skills in itertools.combinations(student_skills, 3) if set.union(*skills) >= problem_skills]
    n_teams_expected = len(team_skills)
    score = min(n_teams / n_teams_expected, 1) if n_teams_expected > 0 else 0
    points = int(score * 100)
    
        fin.close()
        fout.close()
        return {'result': 'AC', 'points': points}

        # Write the evaluation code here.
        # Read the input from fin file object
        # Read the output from fout file object

    except Exception as e:
        fin.close()
        fout.close()

        return {'result': 'WA', 'error': str(e), 'points': 0}

    fin.close()
    fout.close()

    return {'result': 'AC', 'points': points}



