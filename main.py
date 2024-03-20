def calculate_gpa(grades):
    honors_grades = {
        'A+': 4.999,
        'A': 4.666,
        'A-': 4.333,
        'B+': 3.999,
        'B': 3.666,
        'B-': 3.333
    }
    cp_grades = {
        'A+': 4.333,
        'A': 4,
        'A-': 3.667,
        'B+': 3.333,
        'B': 3,
        'B-': 2.667
    }

    total_points_honors = 0
    total_points_cp = 0
    total_courses = len(grades)

    for grade in grades:
        course_name, course_type, course_grade = grade
        if course_type == 'H':
            total_points_honors += honors_grades.get(course_grade, 0)
        elif course_type == 'CP':
            total_points_cp += cp_grades.get(course_grade, 0)

    unweighted_gpa = (total_points_honors - 0.666 + total_points_cp) / total_courses
    weighted_gpa = (total_points_honors + total_points_cp) / (total_courses)
    return unweighted_gpa, weighted_gpa


def main():
    num_courses = int(input("Enter the number of courses: "))
    grades = []

    for i in range(num_courses):
        course_name = input(f"Enter the name of course {i+1}: ")
        course_type = input(f"Enter the type of course (H for Honors, CP for College Prep) for {course_name}: ")
        course_grade = input(f"Enter the grade for {course_name} (A+, A, A-, B+, B, B-): ")
        grades.append((course_name, course_type.upper(), course_grade.upper()))

    unweighted_gpa, weighted_gpa = calculate_gpa(grades)

    print("\nGPA Calculation Results:")
    print(f"Unweighted GPA: {unweighted_gpa:.3f}")
    print(f"Weighted GPA: {weighted_gpa:.3f}")


if __name__ == "__main__":
    main()
