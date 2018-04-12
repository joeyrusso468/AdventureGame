#Adventure Game
default_greeting =  "Hello User, This"
default_greeting += " is an adventure"
default_greeting += " game that takes"
default_greeting += " place in a high"
default_greeting += " school setting"
default_greeting += " where you get to"
default_greeting += " experience the choices"
default_greeting += " of a high school teenager."
default_greeting += " Type any key to continue."
s = input(default_greeting)
uname = ''
uname = input("What's your name? ")
print("Nice to meet you " + uname + "!")

age = int(input("What's your age? "))
print("So, you are already " + str(age) + " years old, " + uname + "!")
if age > 25:
    print('Wow, your pretty old!')
else:
    print('Wow your still pretty young')
print("Here we go!")

run = True
count = 0
count_limit = 25
while run:
#    print(count)
    count += 1
question1= Do you stay home or go to school?
    input(" question1 " + str(count))
    if count > count_limit:
        run = False
print("this is the end")
if(count == 10):
    s = input('Do you want to exit the Adventure game?\n')
    s = s.strip().lower()
if((s == "no")
    or(s == "nope")
    or(s == "no way")
    or(s == "no thanks")
    or(s == "of course not")
    or(s == "hi")
    or(s == "no sir")
    or(s == "sike")
    or(s == "maybe")
    or(s == "stop")):
      count = 0
else:
        if len(uname) < 1:
            print('Good bye, thanks for trying the Adventure Game!')
        else:
            print('Good bye, ' + uname + ' and thanks for trying the Adventure Game!')
