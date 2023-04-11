def HanoiTower(disksNumber, start, end, assistant):
    if disksNumber == 0:
        return
    HanoiTower(disksNumber - 1, start, assistant, end)
    print("Moving:", disksNumber, start, "-->", end)
    HanoiTower(disksNumber - 1, assistant, end, start)


HanoiTower(3, 'A', 'C', 'B')
