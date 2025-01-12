def get_slope(dots):
    slope_1=(dots[1][1]-dots[0][1])/(dots[1][0]-dots[0][0])
    slope_2=(dots[3][1]-dots[2][1])/(dots[3][0]-dots[2][0])
    
    return slope_1, slope_2

def solution(dots):
    x_sort_dots=sorted(dots, key=lambda x: x[0])
    y_sort_dots=sorted(dots, key=lambda x: x[1])
    
    a, b=get_slope(x_sort_dots)
    c, d=get_slope(y_sort_dots)
    
    if a==b or c==d:
        return 1
    return 0