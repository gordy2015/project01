class school(object):
    def __init__(self,name,city):
        self.name = name
        self.city = city

    def school_info(self):
        print('create the school name is %s in %s' % (self.name, self.city))



    def create_class(self):
        class_name = input('pls input class name: ')


class Class(object):
    def __init__(self,name):
        self.name = name

class course(object):
    def __init__(self,name,period,price):
        self.name = name
        self.period = period
        self.price = price


class teacher(object):
    def __init__(self):
        self.name = input('pls input the teacher name: ')
        self.age = input('pls input teacher age: ')
        self.sex = input('pls input teacher sex: ')
        self.course = input('pls input teacher course: ')
        self.tclass = input('pls input teacher class:')
    def show_teacher_info(self):
        print('''
        teacher_name: %s,
        teacher_age: %s,
        "teacher_sex": %s, 
        "teacher_course": %s, 
        "teacher_class": %s
        '''  % (self.name, self.age, self.sex, self.tcourse, self.tclass))
    def teainfo(self):
        print(self.name,self.age,self.sex,self.course,self.tclass)
        teadict = {"teacher_name": teacher_name, "teacher_age": teacher_age, "teacher_sex": teacher_sex, "teacher_course": teacher_course, "teacher_class": teacher_class}



# d =  school('mi','gz')
# print(d.school_info())
# p = school.create_teacher()
#
# print(teacher.show_teacher_info())

teacher()
teacher.teainfo()