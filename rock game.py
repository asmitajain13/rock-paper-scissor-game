import random
#n=input("how many times you want to play:")
a=input("Choose(Rock, Paper, Scissor game):")
c=['Rock', 'Paper', 'Scissor']
d=random.choices(c)
b=''
for i in d:
    b+=i
print("Computer choose: ",b)
if b==a:
    print("Same")
elif b=='Rock':
    if a=='Paper':
        print("user won")
    elif a=='Scissor':
        print("computer won")
elif b=='Paper':
    if a=='Scissor':
        print("user won")
    elif a=='Rock':
        print("computer won")
elif b=='Scissor':
    if a=='Rock':
        print("user won")
    elif a=='Paper':
        print("computer won")

