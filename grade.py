class Progress:
    def inputData(self, subject1, subject2, subject3, subject4, subject5, subject6):

        marks = [subject1, subject2, subject3, subject4, subject5, subject6]
        
        if all(40 <= mark <= 100 for mark in marks):
            total = sum(marks)
            percentage = (total / 600) * 100
            grade = self.Grade(total)
            print(f"Total marks: {total}")
            print(f"Total percentage: {percentage}")
            print(f"Grade: {grade}")
        else:
            total = sum(marks)
            percentage = (total / 600) * 100
            print(f"Total marks: {total}")
            print(f"Total percentage: {percentage}")
            print("Failed")

    def Grade(self, total):
        if total >= 550:
            return "A"
        elif total >= 450:
            return "B"
        elif total >= 350:
            return "C"
        else:
            return "Failed"

if __name__ == "__main__":
    p = Progress()
    p.inputData(50, 50, 50, 50, 50, 50)
