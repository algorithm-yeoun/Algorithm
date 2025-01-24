hour, minute = map(int, input().split())
count=int(input())

count_hour,count_minute=count//60, count%60

hour+=count_hour
minute+=count_minute

print((hour+minute//60)%24, minute%60)