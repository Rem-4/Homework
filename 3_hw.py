#2
def number(a,b):
    if a > b:
        print(a)
    elif b > a:
        print(b)
number(10, 8)

#3
def yes_or_no(a,b):
    if a - b == 135 or -135:
        print('Yes')
    else:
        print('No')
yes_or_no(-135, 0)

#4
def season(month):
    if month in [12, 1, 2]:
        print('Winter')
    elif month in [3, 4, 5]:
        print('Spring')
    elif month in [6, 7, 8]:
        print('Summer')
    elif month in [9, 10, 11]:
        print('Fall')

season(4)

#5
def more_10(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print("Yes")
    else:
        print("No")
more_10(20, 11, 15)