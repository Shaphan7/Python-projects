from app import Data
data = Data('./students_messy.csv')
data.clean()
# Project: Student Grade Analyzer
def handle_subject_lookup(topper=True):
    subject = input("Subject: ").strip()
    try:
        return data.get_subject_student(subject.title(), topper)
    except KeyError:
        return f"'{subject}' not found!"

def help_command():
    return (
        "show-top-students = Top 10 students by total marks\n"
        "show-failed = Students with at least one failed subject\n"
        "show-subject-avg = Average marks for each subject\n"
        "avg-attendance = Average attendance\n"
        "show-attendance-below-75 = Attendance below 75%\n"
        "show-highest-attendance = Top 10 by attendance\n"
        "show-lowest-attendance = Bottom 10 by attendance\n"
        "show-subject-topper = Highest scorer in a subject\n"
        "show-subject-lowest = Lowest scorer in a subject\n"
        "show-stats = Subject statistics\n"
        "export-passed = Export passed students to CSV\n"
        "show = Show all student records\n"
        "help = Show this help message\n"
        "exit = Close the application"
)

# So far my cleanest commands
commands = {
    "show-top-students": data.get_top_students,
    "show-failed": data.get_failed_students,
    "show-subject-avg": data.df[data.subjects].mean,
    "avg-attendance": data.df["Attendance"].mean,
    "show-attendance-below-75": data.get_attendance_below_75,
    "show-highest-attendance": data.get_attendance,
    "show-lowest-attendance": lambda: data.get_attendance(highest=False),
    "show-subject-topper": handle_subject_lookup,
    "show-subject-lowest": lambda: handle_subject_lookup(topper=False),
    "show-stats": data.df[data.subjects].describe,
    "export-passed": data.export_passed,
    "show": data.df.to_string,
    "help": help_command
}

def main():
    while True:
        command = input("Command: ").strip()
        if command in commands:
            # New and better approach
            result = commands[command]()
            if result is not None:
                print(result)
        elif command == "exit":
            print("App closed!")
            break
        else:
            print("Invalid Syntax!")
main()
