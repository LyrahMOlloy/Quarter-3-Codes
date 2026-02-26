class colorz:
    RED = '\033[91m'
    LUVGREEN = '\033[92m'
    PURPLE = "\033[95m" 
    LUVRESET = "\033[0m"
    CYAN = 	"\033[96m"




student = {
    "Name": "",
    "Age" : "",
    "Favorite Subject": "",
}
print(colorz.PURPLE + "Welcome!!!" + colorz.LUVRESET)
name_inp = input("Enter your name!: ")
age_inp = input("Enter your age!: ")
favSubject_inp = input("Enter your favorite subject!: ")

student["Name"] = name_inp
student["Age"] = age_inp
student["Favorite Subject"] = favSubject_inp


print(colorz.LUVGREEN + "Student Record" + colorz.LUVRESET)
for key, value in student.items():
    print(f"{key}: {value}")

