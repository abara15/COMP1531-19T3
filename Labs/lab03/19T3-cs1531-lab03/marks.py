# Author: @abara15 (GitHub)
students = [
    {
        "name": "Matt",
        "homework": [90.0, 97.0, 75.0, 92.0],
        "quizzes": [88.0, 40.0, 94.0],
        "tests": [75.0, 90.0],
    },
    {
        "name": "Mich",
        "homework": [100.0, 92.0, 98.0, 100.0],
        "quizzes": [82.0, 83.0, 91.0],
        "tests": [89.0, 97.0],
    },
    {
        "name": "Mark",
        "homework": [0.0, 87.0, 75.0, 22.0],
        "quizzes": [0.0, 75.0, 78.0],
        "tests": [100.0, 100.0],
    }
]

def marks():
    hw_avg = 0
    q_avg = 0
    t_avg = 0
    x = 0
    while (x < 3):
        hw_avg = hw_avg + sum(students[x]['homework'])
        q_avg = q_avg + sum(students[x]['quizzes'])
        t_avg = t_avg + sum(students[x]['tests'])
        x += 1
    hw_avg = hw_avg/12
    q_avg = q_avg/9
    t_avg = t_avg/6
    marks = {
        "homework" : hw_avg,
        "quiz" : q_avg,
        "tests" : t_avg
    }
    return marks


if __name__ == '__main__':
    marks = marks()
    
    print(f"Average homework mark:", marks['homework'])
    print(f"Average quiz mark:", marks['quiz'])
    print(f"Average test mark:", marks['tests'])