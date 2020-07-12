from collections import defaultdict

# data

user_skill_dict = {
"user_1" :  ["skill_1", "skill_2", "skill_3"],
"user_2" : ["skill_11", "skill_12", "skill_15"],
"user_3" : ["skill_1", "skill_2", "skill_5", "skill_11", "skill_13", "skill_14"],
"user_4": ["skill_11", "skill_13", "skill_14"],
"user_5" : ["skill_11", "skill_13", "skill_14", "skill_16"],
"user_6" : ["skill_12", "skill_13", "skill_18"]
}

project_skill = {
"project_1" : ["skill_1", "skill_2", "skill_3", "skill_4", "skill_5"],
"project_2" : ["skill_1", "skill_3", "skill_4", "skill_6"],
"project_3" : ["skill_2", "skill_3", "skill_8", "skill_9", "skill_10"],
"project_4" : ["skill_11", "skill_13", "skill_14", "skill_16"],
"project_5" : ["skill_12", "skill_13", "skill_18", "skill_5", "skill_14"],
"project_6" : ["skill_1", "skill_2", "skill_5", "skill_11", "skill_13", "skill_14"]
}

group_skill = {
"group_1" : ["skill_1", "skill_2", "skill_3", "skill_4", "skill_5", "skill_6", "skill_7", "skill_8", "skill_9", "skill_10"],
"group_2" : ["skill_11", "skill_12", "skill_13", "skill_14", "skill_15", "skill_16", "skill_17", "skill_18"]
}


flag = False # set True for printing
user = input("Enter which user? ")

print("The recommended skill is: ")

no_of_skill_project = defaultdict(int)
no_of_skill_group = defaultdict(int)
no_of_skill_short_of_project = defaultdict(int)

for skill in user_skill_dict[user]:
    for key,value in project_skill.items():
        if skill in value:
            no_of_skill_project[key] += 1
    for key,value in group_skill.items():
        if skill in value:
            no_of_skill_group[key] += 1

for key,value in no_of_skill_project.items():
    no_of_skill_short_of_project[key] = len(project_skill[key])-value

# list of skills which are only short by 2 in the project
skills = []
t = 0; s = None

no_of_skill_short_of_project = {k: v for k, v in sorted(no_of_skill_short_of_project.items(), key=lambda item: item[1]) if v != 0}

if len(no_of_skill_short_of_project) > 0:
    s,t = next(iter(no_of_skill_short_of_project.items()))

no_of_skill_group = {k: v for k, v in sorted(no_of_skill_group.items(), reverse=True, key=lambda item: item[1])}
flag_ = True

# if short of only 1 skill in the project
if t == 1:
    project = s
    for skill in project_skill[s]:
        if skill not in user_skill_dict[user]:
            print(skill)
            break

# if short of 2 skills in the project
elif t == 2:
    project = s
    for skill in project_skill[s]:
        if skill not in user_skill_dict[user]:
            skills.append(skill)

    for key in no_of_skill_group.keys():
        for skill in skills:
            if skill in group_skill[key]:
                print(skill)
                break

# in all other cases (selects group which has maximum skills)
else:
    for key in no_of_skill_group.keys():
        if flag_:
            for skill in group_skill[key]:
                if skill not in user_skill_dict[user]:
                    print(skill)
                    flag_ = False
                    break
        else:
            break

if flag:
    print(no_of_skill_project)
    print(no_of_skill_group)
    print(no_of_skill_short_of_project)





