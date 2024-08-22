

from grade import Progress
from validation import Validation


if __name__ == "__main__":
    marks = []
    while True:
        n = int(input("Enter the subject marks"))
        if(Validation.validateInput(Validation, n)):
            marks.append(n)
        if len(marks) == 6:
            break
    
    p = Progress()
    p.inputData(marks[0], marks[1], marks[2], marks[3], marks[4], marks[5])