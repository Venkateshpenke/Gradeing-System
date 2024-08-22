class Validation:
 def validateInput(self,m):
    if(m>=0 and m<=100):
        print("valid number")
    else:
        print("Enter the valid marks")
if __name__ == "__main__":
    obj=Validation()
    obj.validateInput(10)