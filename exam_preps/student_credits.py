def students_credits(*args):
    my_dict = {}
    total_obtained_credits = 0
    final_result = ''

    for arg in args:
        course_name, credits, max_test_points, diyan_points = arg.split('-')
        obtained_credits = (int(diyan_points) / int(max_test_points)) * int(credits)
        my_dict[course_name] = obtained_credits
        total_obtained_credits += obtained_credits

    sorted_dict = sorted(my_dict.items(), key=lambda x: -x[1])

    if total_obtained_credits >= 240:
        final_result += f"Diyan gets a diploma with {total_obtained_credits:.1f} credits.\n"

    else:
        final_result += f"Diyan needs {240 - total_obtained_credits:.1f} credits more for a diploma.\n"

    for course, credits in sorted_dict:
        final_result += f"{course} - {credits:.1f}\n"

    return final_result

