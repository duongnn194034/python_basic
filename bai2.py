for ga in range(0, 37):
    cho = 36 - ga
    chan = cho * 4 + ga * 2
    if (chan == 100):
        print('Có', ga, 'con gà và', cho, 'con chó')