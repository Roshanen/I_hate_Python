first_hour, first_min, second_hour, second_min = [
    int(x) for x in input().split()]

minute = ((second_hour * 60) + second_min) - ((first_hour * 60) + first_min)
hour_remain = (minute % 60) > 0
hour = (minute // 60) + hour_remain
day_remain = (hour % 24) > 0
day = (hour // 24) + day_remain

if (hour > 6):
    print(day * 200)
elif (minute > 15) and (hour < 4):
    print(hour * 10)
elif (hour >= 4) and (hour <= 6):
    print(((hour - 3) * 20) + 30)
elif (minute <= 15):
    print(0)
