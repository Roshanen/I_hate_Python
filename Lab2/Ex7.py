'''
7. ให้เขียน function ชื่อ day_of_year(day, month ,year)
โดยมีการคืนค่า คือ day_of_years เป็นวันที่ลําดับที่เท่าใดของปีคริสตศักราช year
– ปีที่เป็น Leap Year เดือนกุมภาพันธ์จะมี 29 วัน
– ให้สร้างฟังก์ชัน is_leap เพื่อตรวจสอบ leap year แยกออกมา และให้ฟังก์ชัน day_of_year
เรียกใช้ is_leap อีกที
'''
def day_of_year(day, month, year):
  total_from_month = [ 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365 ]
  return day + total_from_month[month - 1] + (is_leap(year) if month > 2 else 0)


def is_leap(year):
  return ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
