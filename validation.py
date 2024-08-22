class Validation:
 def validateInput(self,m):
        if m in range(0,101):
            return True
        else:
            print("Please enter a valid number")
            return False
if __name__ == "__main__":
    obj=Validation()
    obj.validateInput(10)