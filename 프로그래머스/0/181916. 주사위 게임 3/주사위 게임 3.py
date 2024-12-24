def solution(a, b, c, d):
    dice = [a,b,c,d]
    dice_set=list(set(dice))
    
    # 4
    if len(dice_set)==1:
        return 1111*dice_set[0]
    
    # (1,3) or (2,2)
    if len(dice_set)==2:
        if dice.count(dice_set[0]) in (1, 3):
            if dice.count(dice_set[0])==1:
                p=dice_set[1]
                q=dice_set[0]
            else:
                p=dice_set[0]
                q=dice_set[1]
            return (10*p+q)**2
        return (dice_set[0]+dice_set[1])*abs(dice_set[0]-dice_set[1])
    
    # (1,1,2)
    if len(dice_set)==3:
        for n in dice_set:
            if dice.count(n) == 2:
                p = n
                qr = [i for i in dice_set if i != p]
                return qr[0] * qr[1]
    
    # (1,1,1,1)
    return min(dice)
            