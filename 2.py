def goal_check():
    condtion = (True and False) or (" " and "")

    if condtion or not condtion:
        return "2024 is my year"
    elif not condtion:
        return "I will continue to procrastinate"
    else:
        return "I'm just a loser"

print(goal_check())