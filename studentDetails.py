rollNumber=[1,2,3,4]
name=["abhijith","akshay","rahul","rashid"]
age=[18,19,20,21]
emailId=["abhijith@gmail.com","akshay@gmail.com","rahul@gmail.com","rashid@gmail.com"]
place=["kasargod","kozhikode","malappuram","kochi"]
def student(i):
    print("name:",name[i-1])
    print("roll number:",rollNumber[i-1])
    print("age:",age[i-1])
    print("email Id:",emailId[i-1])
    print("place:",place[i-1])
while True:
    x=int(input("Enter roll number:"))
    student(x)
    print("")

