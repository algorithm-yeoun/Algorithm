def solution(common):
    # 등차
    if common[-1]-common[-2] == common[-2]-common[-3]:
        return common[-1] + common[-1]-common[-2]
    
    # 등비
    return common[-1]*(common[-1]//common[-2])