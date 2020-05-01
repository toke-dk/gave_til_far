import turtle
import random
import time
import test

wn = turtle.Screen()
#test.countdown()
print("\033c", end="")

y = -500
navne = []
farvel = []
t1l = 0
t2l = 0
t3l = 0
t4l = 0
t5l = 0
farver = ["red", "blue", "green", "orange", "black", "pink", "purple", "grey"]

input("Velkommen til Tokes vildt fede pythonprojekt (Enter)")
print("\033c", end="")
input("Her skal du, som jedi, prøve at være den første i mål (Enter)")
print("\033c", end="")
rand_navne = input("Der er i alt 5 spillere. Hæld og lykke! (Enter)")
if rand_navne == "j":
    for i in range(len(farver) - 5):
        farver.remove(farver[i])
    for i in range(len(farver)):
        farvel.append(farver[i])
        navne.append(i)
else:
    for i in range(5):
        while True:
            navn = input(f"Hvad skal spiller {i + 1}s gamernavn være: ")
            if navn in navne:
                print("Det skal være et navn der ikke er taget")
                continue
            else:
                navne.append(navn)
                break
        while True:
            try:
                print(f"Farver tilbage {farver}")
                farve = input(f"Spiller {i+1} Farve: ")
                farver.remove(farve)
                farvel.append(farve)
                if farve in farvel:
                    break
            except ValueError:
                print("Det skal være en a disse farver")
                continue


en_til = True
while en_til:
    tal = True
    runde = 0
    while tal:
        try:
            gange = int(input("Hvor magne runder skal der spilles: "))
            if gange == 1:
                print("Det tager 15.3 sekunder")
            else:
                print(f"Det tager {14.4 * gange} sekunder")
            tal = False
        except ValueError:
            print("Det skal være et heltal tal")
    start_tid = time.time()
    for i in range(gange):
        runde = runde + 1
        print(f"Runder {runde}/{gange}", end='\r')
        ots = time.time()
        t1 = turtle.Turtle()
        t1.shape("turtle")
        t1.penup()
        t1.goto(-80, y)
        t1.left(90)
        t1.color(farvel[0])
        t2 = turtle.Turtle()
        t2.shape("turtle")
        t2.penup()
        t2.left(90)
        t2.goto(-40, y)
        t2.color(farvel[1])
        t3 = turtle.Turtle()
        t3.shape("turtle")
        t3.penup()
        t3.left(90)
        t3.goto(0, y)
        t3.color(farvel[2])
        t4 = turtle.Turtle()
        t4.shape("turtle")
        t4.penup()
        t4.left(90)
        t4.goto(40, y)
        t4.color(farvel[3])
        t5 = turtle.Turtle()
        t5.shape("turtle")
        t5.penup()
        t5.left(90)
        t5.goto(80, y)
        t5.color(farvel[4])

        t1.pendown()
        t2.pendown()
        t3.pendown()
        t4.pendown()
        t5.pendown()
        t1.pensize(5)
        t2.pensize(5)
        t3.pensize(5)
        t4.pensize(5)
        t5.pensize(5)


        for i in range(50):
            turtle.hideturtle()
            h = random.randint(5, 40)
            t1.forward(h)
            t1l = t1l + h
            q = random.randint(5, 40)
            t2.forward(q)
            t2l = t2l + q
            w = random.randint(5, 40)
            t3.forward(w)
            t3l = t3l + w
            e = random.randint(5, 40)
            t4.forward(e)
            t4l = t4l + e
            r = random.randint(5, 40)
            t5.forward(r)
            t5l = t5l + r
        time.sleep(2)
        turtle.clearscreen()
        otsl = time.time()
    slut_tid = time.time()
    player_distance = {navne[0]: t1l, navne[1]: t2l, navne[2]: t3l, navne[3]: t4l, navne[4]: t5l}
    player_color = {navne[0]: farvel[0], navne[1]: farvel[1], navne[2]: farvel[2], navne[3]: farvel[3], navne[4]: farvel[4]}
    for i in range(5):
        winner = max(player_distance, key=player_distance.get)
        spiller_farve = player_color.pop(winner)
        print(f"{i + 1}:{spiller_farve}, {winner}")
        del player_distance[winner]
    print(f"Tid i alt: {float(slut_tid-start_tid)} på {runde} runder")
    igen = input("En gang til? J/N: ")
    if igen.lower() == "j" or igen.lower() == "ja":
        del player_distance
        del player_color
        continue
    else:
        en_til = False