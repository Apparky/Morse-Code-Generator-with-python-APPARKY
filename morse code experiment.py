import winsound
import time


def string_splitter(s_value):
    string = s_value
    my_list = []

    for s in string:
        if s == '':
            my_list.append('_')

        else:
            my_list.append(s)
            my_list.append('_')

    print(my_list)
    return my_list


def morse_generator(inputs):
    values = inputs

    for v in values:
        time.sleep(.5)
        if v == '_' or v == ' ':
            time.sleep(.8)
            print('.')

        elif v == "A" or v == "a":
            winsound.Beep(3000, 130)
            time.sleep(.35)
            winsound.Beep(3000, 300)
            print(v)

        elif v == "B" or v == "b":
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            print(v)

        elif v == "C" or v == "c":
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            print(v)

        elif v == "D" or v == "d":
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            print(v)

        elif v == "E" or v == "e":
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            print(v)

        elif v == "F" or v == "f":
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            print(v)

        elif v == "G" or v == "g":
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            print(v)

        elif v == "H" or v == "h":
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            print(v)

        elif v == "I" or v == "i":
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            print(v)

        elif v == "J" or v == "j":
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 300)
            print(v)

        elif v == "K" or v == "k":
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 300)
            print(v)

        elif v == "L" or v == "l":
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            print(v)

        elif v == "M" or v == "m":
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 300)
            print(v)

        elif v == "N" or v == "n":
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            print(v)

        elif v == "O" or v == "o":
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 300)
            print(v)

        elif v == "P" or v == "p":
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            print(v)

        elif v == "Q" or v == "q":
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 300)
            print(v)

        elif v == "R" or v == "r":
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            print(v)

        elif v == "S" or v == "s":
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            print(v)

        elif v == "T" or v == "t":
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            print(v)

        elif v == "U" or v == "u":
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            print(v)

        elif v == "V" or v == "v":
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 300)
            print(v)

        elif v == "W" or v == "w":
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 300)
            print(v)

        elif v == "X" or v == "x":
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 300)
            print(v)

        elif v == "Y" or v == "y":
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 300)
            print(v)

        elif v == "Z" or v == "z":
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 300)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            time.sleep(0.25)
            winsound.Beep(3000, 130)
            print(v)


while True:
    value = str(input("Enter anything: "))
    strings = string_splitter(value)
    morse_generator(strings)
