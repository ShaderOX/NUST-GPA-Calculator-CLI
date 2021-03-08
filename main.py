import json
from typing import List, Dict

COURSES_FILE = 'courses.json'
GRADES_FILE = 'grades.json'


def main():
    grades = load_grades()

    # Loads the grades as a list of python dictionaries
    with open(COURSES_FILE, 'r') as f:
        courses = json.load(f)

    total_credit_hours = 0
    your_credit_hours = 0
    for course in courses:
        course_credit_hours = course.get('credit_hours')
        total_credit_hours += course_credit_hours
        your_credit_hours += grades.get(course.get('grade')) \
            * course_credit_hours

    print("Your GPA is:", round(your_credit_hours / total_credit_hours, 3))


def load_grades() -> List[Dict]:
    """ Loads the grades from the GRADES_FILE and returns the dictionary to the caller function """
    with open(GRADES_FILE, 'r') as f:
        grades = json.load(f)

    return grades


if __name__ == '__main__':
    main()
