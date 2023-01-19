'''
9. จากโปรแกรมในข้อ 8 ให้เขียนฟังก์ชัน date_diff เพิ่มเติม โดยให้มีการตรวจสอบ
– วันที่ต้องเป็นวันที่ถูกต้องของเดือนนั้นๆ
– เดือนต้องอยู่ระหว่าง 1-12
– เดือนกุมภาพันธ์ของปีที่มี Leap Year เท่านั้นที่จะมี 29 วันได้
– หากข้อมูล Input ผิดพลาด ให้ Return -1
'''
day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def check_day(date):
    return day_in_month[date[1]] + 1 >= date[0] if date[1] == 2 and is_leap(date[2]) else day_in_month[date[1]] >= date[0]


def check_month(date):
    return check_day(date) if 0 < date[1] < 13 else 0


def check_year(date):
    return check_month(date) if date[2] > 0 else 0


def check_date(date):
    return check_year(date)


def day_of_year(date):
    return int(date[0]) + sum(day_in_month[:date[1]]) + (is_leap(date[2])if int(date[1]) > 2 else 0)


def day_in_year(year):
    return 365 + is_leap(year)


def is_leap(year):
    return ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)


def diff_from_year(year1, year2):
    return sum([day_in_year(i) for i in range(year1, year2)])


def date_diff(date1, date2):
    date1 = [int(x) for x in date1.split("-")]
    date2 = [int(x) for x in date2.split("-")]
    if check_date(date1) and check_date(date2):
        return day_of_year(date2) - day_of_year(date1) + diff_from_year(date1[2], date2[2]) + 1
    else:
        return -1
