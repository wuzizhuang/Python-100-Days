from time import sleep


class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def study(self,course_name):
        print('%s正在学习%s' % (self.name,course_name))

class Clock(object):
    def __init__(self,hour=0,minute=0,second=0):
        self._hour = hour
        self._minute = minute
        self._second = second
    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0
    def show(self):
        return '%02d:%02d:%02d' % (self._hour,self._minute,self._second)


def main():
    stu1 = Student('骆昊',38)
    stu1.study('Python程序设计')
    stu2 = Student('王大锤',15)
    stu2.study('思想品德')
    clock = Clock(23,59,58)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

if __name__ =='__main__':
    main()