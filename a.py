import requests
import random
import time 

problems = requests.get("https://codeforces.com/api/problemset.problems").json()

problems = problems["result"]["problems"]


database = {
    1000 : [],
    1100: [],
    1200 : [],
    1300: [],
    1400 : [],
    1500: [],
    1600 : [],
    1700: [],
    1800: [],
    1900: []
}

for problem in problems:
    rating = problem.get("rating")
    if rating in database.keys() and problem["contestId"] and problem["contestId"] > 1000:
        database.get(rating).append([str(problem["contestId"]), problem["index"]])

contest_new = []
members = ["Denis_64", "ermukanoff", "Fanarill", "Keremzero4", "KirillK1", "Klyaksa", "Minder", "osoka_123", "Whoami2003"]

for variable_rating in database.keys():
    f = True
    while f:
        task = random.choice(database.get(variable_rating))
        f = False
        for i in range (0, len(members)):
            member = members[i]
            req = "https://codeforces.com/api/user.status?handle=" + member
            check = requests.get(req).json()
            time.sleep(2)
            check = check.get("result")
            for submission in check:
                submission = submission.get("problem")
                if submission.get("contestId") == task[0] and submission.get("index") == task[1]:
                    f = True
                    break
            if f:
                break
    contest_new.append(task[0] + task[1])
    print("Task added successfully")
random.shuffle(contest_new)
for task in contest_new:
    print(task)


