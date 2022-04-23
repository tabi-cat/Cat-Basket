#FOR LOOP - Cats in the Basket

print(' ')

print('I place my basket on the table.')
print(' ')

total = 0

for counter in range (1,7):
    score = int(input('Enter your guesses for how many cats are in my basket: '))
    total = score + total

print(' ')
print('Curiously, your guesses add up to ',total,'cats.')
print('Now, let me tell you how many cats are in my basket.')

avenum = total/6
avecat = round(avenum,0)

print(' ')
print('I open my basket and the cats peer out.')
print(' ')
print('There are ',avecat,'cats in my basket.')
print('Well done if one or more of your guesses were correct.')
