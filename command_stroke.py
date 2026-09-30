import random
import sys
import keyword
import time
import pickle
import turtle
import subprocess
from tkinter import*
print(" v2.02 cmd  python version:", sys.version, 'related to the Windows operating system',  )
while True:
    user = input("hey user type special password:")
    print("password: ==522452==")
    if user == '==522452==':
        print("correct!")
        print('''type 'guide' for guides in this program ''')
        break
    else:
        print("not true")
while True:
    command = input("command:")
    if command == 'random_py':
        numbers_of_ruletka = input('what number you need for roll? 4, 2 or 6:')
        if numbers_of_ruletka == '2':
            roll = input('first what you need for roll:')
            roll_2 = input('second what you need for roll:')
            rolls = [roll, roll_2]
            rolch = random.choice(rolls)
            print(rolch)
        elif numbers_of_ruletka == '4':
            roll = input('first what you need for roll:')
            roll_2 = input('second what you need for roll:')
            roll_3 = input('third what you need for roll:')
            roll_4 = input('fourd what you need for roll:')
            rolls = [roll, roll_2, roll_3, roll_4]
            rolch = random.choice(rolls)
            print(rolch)
        elif numbers_of_ruletka == '6':
            roll = input('1st what you need for roll:')
            roll_2 = input('2nd what you need for roll:')
            roll_3 = input('3rd what you need for roll:')
            roll_4 = input('4th what you need for roll:')
            roll_5 = input('5th what you need for roll:')
            roll_6 = input('6th what you need for roll:')
            rolls = [roll, roll_2, roll_3, roll_4, roll_5, roll_6]
            rolch = random.choice(rolls)
            print(rolch)
    elif command == 'keywords_py':
        print(keyword.kwlist, 'here your  keywords')
    elif command == 'nowtime_py':
        print(time.asctime())
    elif command == 'open_py':
        opent = input('type your file:')
        openx = open(opent)
        openy = openx.read()
        print('this is text in a file', openy)
    elif command == 'save_list':
        yourlist = input('what words you need to be in list:')
        save = open('c:\\Users\\Artur\\test.txt',  'wb')
        pickle.dump(yourlist, save)
        save.close()
        print('''saved to txt file 'test.txt' in c:\\users\\Artur\\ ''')
    elif command == 'load_list':
        load_file = open('c:\\users\\Artur\\test.txt', 'rb')
        load_list = pickle.load(load.file)
        load_file.close()
        print(load_list)
    elif command == 'turtle_star':
        t = turtle.Pen()
        for x in range(1, 9):
            t.speed(40)
            t.forward(100)
            t.left(225)
    elif command == 'turtle_star2':
        t = turtle.Pen()
        for x in range(1, 38):
            t.speed(40)
            t.forward(100)
            t.left(175)
    elif command == 'turtle_car':
        t = turtle.Pen()
        t.reset()
        t.speed(10)
        t.color(1, 0, 0)
        t.begin_fill()
        t.forward(100)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.left(90)
        t.forward(60)
        t.left(90)
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.end_fill()
        t.color(0, 0, 0)
        t.up()
        t.forward(10)
        t.down()
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        t.setheading(0)
        t.up()
        t.forward(90)
        t.right(90)
        t.forward(10)
        t.setheading(0)
        t.begin_fill()
        t.down()
        t.circle(10)
        t.end_fill()
    elif command == 't.reset':
        t = turtle.Pen()
        t.reset()
    elif command == 'guide':
        guides = ['commands', 'python_commands']
        print(guides)
        question = input('choose what guide in list you need:')
        if question == 'commands':
            print('commands:  random_py, keywords_py, nowtime_py, open_py, save_list, load_list, turtle_star, turtle_star2, turtle_car, calculator')
        print()
    

    elif command == 'create_rec':
        tk = Tk()
        canvas = Canvas(tk, width=400, height=400)
        canvas.pack()
        def random_rectagle(width, height, fill_color):
            x1 = random.randrange(width)
            y1 = random.randrange(height)
            x2 = random.randrange(x1 + random.randrange(width))
            y2 = random.randrange(y1 + random.randrange(height))
            canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)
        colors = ['red', 'blue', 'yellow', 'green', 'brown', 'black', 'orange']
        rec_color =  random.choice(colors) #chooses color for rectagle
        random_rectagle(400, 400, rec_color) #creates rectagle
    elif command == "calculator":
        what_use = input("Write the mathematical symbol you will use in the calculator for example +, %, *, -:")
        if what_use == '*':
            cal1 = input("type 1st number of example:")
            cal2 = input("type 2nd number of example:")
            cal1 = int(cal1)
            cal2 = int(cal2)
            no =  cal1 * cal2
            print("answer:", no)
        elif what_use == '%':
            cal1 = input("type 1st number of example:")
            cal2 = input("type 2nd number of example:")
            cal1 = int(cal1)
            cal2 = int(cal2)
            no =  cal1 / cal2
            print("answer:", no)
        elif what_use == '+':
            cal1 = input("type 1st number of example:")
            cal2 = input("type 2nd number of example:")
            cal1 = int(cal1)
            cal2 = int(cal2)
            no =  cal1 + cal2
            print("answer:", no)

        elif what_use == '-':
            cal1 = input("type 1st number of example:")
            cal2 = input("type 2nd number of example:")
            cal1 = int(cal1)
            cal2 = int(cal2)
            no = cal1 - cal2
            print("answer:", no)
    elif command == 'run_program':
        pass
        
    
    else:
        print('Error 404: This command has been removed or does not exist ')
        
        
    
