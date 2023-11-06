import random
print('''
Welcome to Slot Machine!
You have $100, spin = -$1, combinations:
🎰🎰🎰 - $100
🔔🔔🔔 - $75
🍇🍇🍇 - $50
🍊🍊🍊 - $25
🍋🍋🍋 - $10
🍒🍒🍒 - $5
[y/yes]: Spin | [n/no]: End
Blank input = "yes"
''')
cash = 100
items = ['🎰','🔔','🍇','🍊','🍋','🍒']
game = True
while game == True and cash != 0:
    run = input().lower()
    if run == 'y' or run == 'yes' or run == '':
        cash -= 1
# 1- First  |w1|w2|w3|
# 2- Second |w4|w5|w6| (Main)
# 3- Third  |w7|w8|w9|
        # 2- Second (Main)          
        w4 = random.randint(0,5)
        w5 = random.randint(0,5)
        w6 = random.randint(0,5)
        # 1- First
        w1 = w4 - 1
        w2 = w5 - 1
        w3 = w6 - 1
        # 3- Third
        if w4 != 5:
            w7 = w4 + 1
        else:
            w7 = 0
        if w5 != 5:
            w8 = w5 + 1
        else:
            w8 = 0
        if w6 != 5:
            w9 = w6 + 1
        else:
            w9 = 0
        # Win combinations
        if w4 == w5 == w6:
            if w4 == 0:
                cash += 100
                print('You win $100')
            if w4 == 1:
                cash += 75
                print('You win $75')
            if w4 == 2:
                cash += 50
                print('You win $50')
            if w4 == 3:
                cash += 25
                print('You win $25')
            if w4 == 4:
                cash += 10
                print('You win $10')
            if w4 == 5:
                cash += 5
                print('You win $5')
        # Showcase
        else:
            print('You lose')
        print(items[w1]+items[w2]+items[w3])
        print(items[w4]+items[w5]+items[w6])
        print(items[w7]+items[w8]+items[w9])
        print('Cash: $'+str(cash))
    elif run == 'n' or run == 'no':
        game = False
    else:
        print('Wrong input')
