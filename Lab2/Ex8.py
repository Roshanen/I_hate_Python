'''
8. จากโปรแกรมในข้อ 7 ให้เขียนฟังก์ชัน เพิ่มเติมเป็น date_diff
– รับข้อมูลในรูปแบบ “dd-mm-yyyy” เช่น

date_diff(“1-1-2018”, “1-1-2020”) จะได้ 731 วัน
date_diff(“25-12-1999”, “9-3-2000”) จะได้ 76 วัน
– ให้เขียนฟังก์ชัน day_in_year โดยจะส่งค่าจํานวนวันของปี (365 หรือ 366) โดยรับข้อมูลเป็น ปี
– ส่งคืนข้อมูลเป็นจํานวนวันตั้งแต่วันที่แรก จนถึงวันที่สอง โดยรวมทั้ง 2 วันนั้นเข้าไปด้วย
– ให้สมมติว่าวันแรก จะต้องมาก่อนวันที่สองเสมอ ดังนั้นไม่ต้องตรวจสอบ
'''
def day_of_year(date):
  total_from_month = [ 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365 ]
  return int(date[0]) + total_from_month[date[1] - 1] + (is_leap(date[2])if int(date[1]) > 2 else 0)


def day_in_year(year):
  return 365 + is_leap(year)


def is_leap(year):
  return ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)


def date_diff(date1, date2):
  date1 = [int(x) for x in date1.split("-")]
  date2 = [int(x) for x in date2.split("-")]
  total_from_year = 0
  for i in range(int(date1[2]), int(date2[2])):
    total_from_year += day_in_year(i)
  return day_of_year(date2) - day_of_year(date1) + total_from_year + 1
