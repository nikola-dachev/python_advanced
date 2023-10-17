def gather_credits(needed_credits, *args):
    my_courses = []
    gathered_credits = 0
    final_result = ''
    for course_name, course_credits in args:

        if gathered_credits >= needed_credits:
            break

        if course_name not in my_courses:
            my_courses.append(course_name)
            gathered_credits += course_credits

    if gathered_credits >= needed_credits:
        final_result += f"Enrollment finished! Maximum credits: {gathered_credits}.\n"
        final_result += f"Courses: {', '.join(sorted(my_courses))}"
        return final_result

    final_result += f"You need to enroll in more courses! You have to gather {needed_credits - gathered_credits} credits more."
    return final_result


print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
