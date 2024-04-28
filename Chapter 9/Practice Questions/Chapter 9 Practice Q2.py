def game():
    return 56
score=game()

with open('highscore.txt') as f:
    highscore=int(f.read())
    if highscore<score:
        with open('highscore.txt','w') as f:
            newhighscore=f.write(str(score))
    else:
        print("Highscore not reached")