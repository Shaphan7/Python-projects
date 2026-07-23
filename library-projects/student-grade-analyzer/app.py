import pandas as pd

class Data:
    def __init__(self, file):        
        df = pd.read_csv(file)
        self.df = df.set_index("Name")
        self.subjects = ["Math", "Physics", "Chemistry", "English"]

    # The real pandas usage
    def clean(self):
        self.df = self.df.replace({'absent': 0}).apply(pd.to_numeric, errors="coerce")
        self.df = self.df.dropna()

        self.df.index = self.df.index.str.strip().str.lower().str.title()

        self.df = self.df[
            (self.df[self.subjects] >= 0).all(axis=1) & 
            (self.df[self.subjects] <= 100).all(axis=1)
        ]

        self.df = self.df[~self.df.index.duplicated(keep='first')]

    def get_top_students(self):
        new_df = self.df.copy()
        new_df["Total"] = new_df[self.subjects].sum(axis=1)
        new_df = new_df[["Math", "Physics", "Chemistry", "English", "Total"]].sort_values(ascending=False, by="Total")
        return new_df[:10]
    
    def get_failed_students(self):
        return self.df[(self.df[self.subjects] < 40).any(axis=1)]

    # why did I add 75? because my project description told me to.
    def get_attendance_below_75(self):
        return self.df[(self.df["Attendance"] < 75)]
    
    def get_attendance(self, highest=True):
        new_df = self.df.copy()
        if highest:
            new_df = new_df.sort_values(ascending=False, by="Attendance")
        else:
            new_df = new_df.sort_values(by="Attendance")
        return new_df[:10]
    def get_subject_student(self, subject, topper=True):
        if topper:
            student = self.df[subject].idxmax()
        else:
            student = self.df[subject].idxmin()
        return self.df.loc[student]
    def export_passed(self):
        new_df = self.df.copy()
        failed_students = (new_df[self.subjects] < 40).any(axis=1)
        new_df = new_df[~failed_students]
        new_df.to_csv("./students_passed.csv")
        return "File has been successfully exported!"