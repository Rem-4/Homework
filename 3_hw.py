#2
def chislo(a,b):
    if a > b:
        print(a)
    elif b > a:
        print(b)
chislo(10, 8)

#3
def yes_or_no(a,b):
    if a - b == 135 or -135:
        print('Yes')
    else:
        print('No')
yes_or_no(-135, 0)

#4
def season(e):
    if e == 12 or e == 1 or e == 2:
        print('Winter')
    elif e == 3 or e == 4 or e == 5:
        print('Spring')
    elif e == 6 or e == 7 or e == 8:
        print('Summer')
    elif e == 9 or e == 10 or e == 10:
        print('Fall')
season(12)

#5
def bolshe(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print("Yes")
    else:
        print("No")
bolshe(20, 11, 15)