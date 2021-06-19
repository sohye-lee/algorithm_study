[h, m] = input("").split(" ")
hour = int(h)
minute = int(m)

def set_alarm(hour, minute):
    if minute >= 45:
        minute = minute - 45
    else:
        minute = minute + 60 - 45
        if hour == 0:
            hour = 23
        else:
            hour = hour - 1
    print(hour, minute)


set_alarm(hour, minute)