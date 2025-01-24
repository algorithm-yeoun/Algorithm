a,b,c=map(int, input().split())

if a==b==c:
    answer=10000+a*1000
elif a==b or b==c:
    answer=1000+b*100
elif a==c:
    answer=1000+a*100
else:
    max_dice=max(a,b,c)
    answer=max_dice*100

print(answer)