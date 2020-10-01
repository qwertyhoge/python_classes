import random

print('roll XdY dice.')
dice_cnt = int(input('X: '))
surfaces = int(input('Y: '))

print('will roll {0}d{1}.'.format(dice_cnt, surfaces))

dice_total = 0
for i in range(dice_cnt):
    roll = random.randint(1, surfaces)
    print('{0} time roll: {1}'.format(i + 1, roll))
    dice_total += roll

print(dice_total)
