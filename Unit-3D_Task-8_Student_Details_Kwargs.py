
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_details(
    Name="Lasya",
    Age=18,
    Branch="CSE Cyber",
    College="Engineering College"
)
