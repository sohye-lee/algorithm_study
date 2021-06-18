year = input("")

def leap_year(year):
    year = int(year)

    if year < 0 or year > 4000:
        return
    
    if year%4 != 0:
        return 0
    else: 
        if year%400 == 0:
            return 1
        elif year%100 == 0:
            return 0
        else:
            return 1

print(leap_year(year))
