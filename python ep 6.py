class School:
    # attribute
    schoolName = 'สว่างบริบูรณ์วิทยา'

    # Constructor
    def __init__(self):
        print('ให้แสดงข้อความนี้ เมื่อมีการสร้าง Instance')
        
    # Method
    def hello(self):
        print('สวัสดีตอนเช้า ยินดีต้อนรับนักเรียนทุกคน')

    def teach(self, subject):
        print(f'โรงเรียนนี้ เปิดสอนวิชา {subject}')

class Student(School):
    def __init__(self, fullname, level, scores):
        self.fullname = fullname
        self.level = level
        self.scores = scores

    def checkGrade(self, subject):
        if self.scores >= 80:
            print(f'วิชา {subject} ได้เกรด A')
        elif self.scores >= 70:
            print(f'วิชา {subject} ได้เกรด B')
        elif self.scores >= 60:
            print(f'วิชา {subject} ได้เกรด C')
        elif self.scores >= 50:
            print(f'วิชา {subject} ได้เกรด D')
        elif self.scores >= 40:
            print(f'วิชา {subject} ได้เกรด F')

# instance
school = School()
print(f'สว่างบริบูรณ์วิทยา: {school.schoolName}')
school.hello()
school.teach('Mathematics')

print('###############################')
student01 = Student('jacob matin', 1, 75)
student01.hello()
print(f'โรงเรียน {student01.schoolName}')
print(f'ชื่อนักเรียน {student01.fullname}')
print(f'ระดับชั้น {student01.level}')
print(f'คะแนนสอบ {student01.scores}')
student01.checkGrade('Mathematics')

print('###############################')
student02 = Student('edward newgate', 7, 90)
student02.hello()
print(f'โรงเรียน {student02.schoolName}')
print(f'ชื่อนักเรียน {student02.fullname}')
print(f'ระดับชั้น {student02.level}')
print(f'คะแนนสอบ {student02.scores}')
student02.checkGrade('Mathematics')

print('###############################')
student03 = Student('tiger gai', 12, 49)
student03.hello()
print(f'โรงเรียน {student03.schoolName}')
print(f'ชื่อนักเรียน {student03.fullname}')
print(f'ระดับชั้น {student03.level}')
print(f'คะแนนสอบ {student03.scores}')
student03.checkGrade('Mathematics')
