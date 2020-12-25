from django.db import models

GENDER = (('male','女'),('female','男'))
DEPT = (('信息工程学院','信息工程学院'),)
MAJOR =(
    ('计算机网络技术','计算机网络技术'),
    ('计算机应用技术','计算机应用技术'),
    ('软件技术','软件技术'),
    ('云计算技术与应用','云计算技术与应用'),
    ('大数据技术与应用','大数据技术与应用'),
    ('网络安全与管理','网络安全与管理'),
    ('电子信息工程技术','电子信息工程技术'),
    )
# CLASS=(('2019','2019'),('2020','2020'),('2021','2021'),)
# Freshman, sophomore, Junior

SUBJECT =(
    ('Python','Python程序设计'),
    ('C','C语言程序设计'))

class Student(models.Model):
    id=models.CharField('学号',max_length=32,primary_key=True)
    name=models.CharField('姓名',max_length=32)
    password=models.CharField('密码',max_length=32,default='123456')
    gender=models.CharField('性别',max_length=32,choices=GENDER,default='男')
    dept=models.CharField('学院',max_length=32,choices=DEPT,default='信息工程学院')
    major=models.CharField('专业',max_length=32,choices=MAJOR,default='计算机网络技术')
    # Class=models.CharField('班级',max_length=32,choices=CLASS),
    email=models.EmailField('邮箱',unique=True)
    birth=models.DateField('出生日期')
    telephone = models.CharField('电话', max_length=32)            

    class Meta:
        db_table='student'
        verbose_name='学生'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.id

class Teacher(models.Model):
    id=models.CharField("教工号",max_length=32,primary_key=True)
    name=models.CharField('姓名',max_length=32)
    password=models.CharField('密码',max_length=32,default='123456')
    gender=models.CharField('性别',max_length=32,choices=GENDER,default='男')
    dept=models.CharField('学院',max_length=32,choices=DEPT,default='信息工程学院')
    email=models.EmailField('邮箱',default=None)
    birth=models.DateField('出生日期')
    telephone = models.CharField('电话', max_length=32)

    class Meta:
        db_table='teacher'
        verbose_name='教师'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class Question(models.Model):
    ANSWER=(
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D'),
    )
    LEVEL={
        ('1','easy'),
        ('2','general'),
        ('3','difficult'),
    }
    id = models.AutoField(primary_key=True)
    subject = models.CharField('科目',choices=SUBJECT, max_length=32,default='Python')
    title = models.TextField('题目')
    optionA=models.CharField('A选项',max_length=50)
    optionB=models.CharField('B选项',max_length=50)
    optionC=models.CharField('C选项',max_length=50)
    optionD=models.CharField('D选项',max_length=50)
    answer=models.CharField('答案',max_length=32,choices=ANSWER)
    level=models.CharField('等级',max_length=32,choices=LEVEL,default='1')
    score=models.IntegerField('分数',default=1)

    class Meta:
        db_table='question'
        verbose_name='单项选择题'
        verbose_name_plural=verbose_name

    def __str__(self):
        return '<%s:%s>'%(self.subject,self.title);

class Paper(models.Model):
    id = models.AutoField(primary_key=True)
    #题号qid 和题库为多对多的关系
    qid=models.ManyToManyField(Question)
    tid=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    subject=models.CharField('科目',choices=SUBJECT,max_length=20,default='python')
    major=models.CharField('考卷适用专业',choices=MAJOR,max_length=32)
    examtime=models.DateTimeField() 

    class Meta:
        db_table='paper'
        verbose_name='试卷'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.major

# Class schedule 课表 太复杂没做成
class Schedule(models.Model):
    tid=models.ManyToManyField(Teacher)
    dept=models.CharField('学院',max_length=32,choices=DEPT,default='信息工程学院')
    major=models.CharField('专业',choices=MAJOR,max_length=32,default='计算机网络技术')
    Class=models.CharField('班级',max_length=32)
    subject=models.CharField('科目',choices=SUBJECT,max_length=20,default='python')


class Grade(models.Model):
    sid=models.ForeignKey(Student,on_delete=models.CASCADE,default='')
    subject=models.CharField('科目',choices=SUBJECT,max_length=32,default='python')
    grade=models.IntegerField()

    def __str__(self):
        return '<%s:%s>'%(self.sid,self.grade);

    class Meta:
        db_table='grade'
        verbose_name='成绩'
        verbose_name_plural=verbose_name


