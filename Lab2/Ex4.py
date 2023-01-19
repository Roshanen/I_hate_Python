'''
4. ให้เขียนโปรแกรมเพื่อรับข้อมูล 1 บรรทัด ที่ประกอบด้วยจํานวนเต็มหลายจํานวน (คั่นด้วยช่องว่าง)
ให้ส่งคืนว่ามีจํานวนที่เป็นลบกี่จํานวน โดยใช้ List comprehension
ให้เขียนในฟังก์ชัน count_minus(str) แล้ว return เป็นคําตอบ
'''
def count_minus(stra):
    return len([int(i) for i in stra.split() if int(i) < 0])
