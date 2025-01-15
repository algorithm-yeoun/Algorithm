angle1 = int(input())
angle2 = int(input())

sum_angle = angle1+angle2-360*((angle1+angle2)//360) if (angle1+angle2)>=360 else angle1+angle2
print(sum_angle)