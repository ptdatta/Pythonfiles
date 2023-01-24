
def funargs(normal, *argsrohan, **kwargsbala):  #normal always comes first
    print(normal)
    for item in argsrohan:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargsbala.items():
        print(f"{key} is a {value}")



har = ["Harry", "Rohan", "Skillf", "Hammad",
       "Shivam", "The programmer"]
normal = "I am a normal Argument and the students are:"
kw = {"Rohan": "Monitor", "Harry": "Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam": "Cook"}
funargs(normal, *har, **kw)

