from django.shortcuts import render,redirect
from django import forms
from django.http import HttpResponse
from django.contrib.auth import logout
from .models import Student,Teacher,Paper,Question,Grade
from .forms import StudentForm,TeacherForm,RegisterForm

def index(request):
    return render(request,'exam/index.html')

def logout(request):
    return redirect('/exam')

def register(request):
    if request.session.get('is_login', None):
        return redirect('/exam/')

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            id = register_form.cleaned_data.get('id')
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')
            dept = register_form.cleaned_data.get('dept')
            major = register_form.cleaned_data.get('major')
            birth = register_form.cleaned_data.get('birth')
            telephone = register_form.cleaned_data.get('telephone')

            if password1 != password2:
                message = '两次输入的密码不同！'                
            else:
                same_name_user = Student.objects.filter(id=id)
                if same_name_user:
                    message = '学生已经存在'
                else:
                    same_email_user = Student.objects.filter(email=email)
                    if same_email_user:
                        message = '该邮箱已经被注册了！'
                    
                    else:

                        new_user = Student()
                        new_user.id=id
                        new_user.name = username
                        new_user.password = password1
                        new_user.email = email
                        new_user.sex = sex
                        new_user.dept = dept
                        new_user.major = major
                        new_user.birth = birth
                        new_user.telephone = telephone
                        new_user.save()

                        return redirect('/exam/')

    register_form = RegisterForm()
    return render(request, 'exam/register.html', locals())

def loginStudent(request):
    if request.method == 'POST':
        login_form = StudentForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            sn = login_form.cleaned_data.get('sn')
            password = login_form.cleaned_data.get('password')

            try:
                student = Student.objects.get(id=sn)
                print(sn,student.id)
            except :
                message = '学生不存在！'                

            else:
                if student.password == password:
                    #查询考试信息 学生所在专业的所有试卷
                    paper=Paper.objects.filter(major=student.major)
                    
                    #查询成绩信息
                    grade=Grade.objects.filter(sid=student.id)
                    context = {'student':student,'paper':paper,'grade':grade}
                    return render(request,'exam/studentLogin.html', context=context)
                else:
                    message = '密码不正确！'              

    login_form = StudentForm()
    return render(request, 'exam/loginStudent.html', locals())


def loginTeacher(request):
    if request.method == 'POST':
        login_form = TeacherForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            sn = login_form.cleaned_data.get('sn')
            password = login_form.cleaned_data.get('password')

            try:
                teacher = Teacher.objects.get(id=sn)
                if teacher.password == password:
                    # 实现成绩统计功能
                    #在试卷表 paper 找到该老师发布的试题
                    paper=Paper.objects.filter(tid=teacher.id)

                    data1=Grade.objects.filter(subject='python',grade__lt=60).count()
                    data2=Grade.objects.filter(subject='python',grade__gte=60,grade__lt=70).count()
                    data3=Grade.objects.filter(subject='python', grade__gte=70, grade__lt=80).count()
                    data4=Grade.objects.filter(subject='python', grade__gte=80, grade__lt=90).count()
                    data5=Grade.objects.filter(subject='python', grade__gte=90).count()

                    data6 = Grade.objects.filter(subject='数据库原理', grade__lt=60).count()
                    data7= Grade.objects.filter(subject='数据库原理', grade__gte=60, grade__lt=70).count()
                    data8= Grade.objects.filter(subject='数据库原理', grade__gte=70, grade__lt=80).count()
                    data9 = Grade.objects.filter(subject='数据库原理', grade__gte=80, grade__lt=90).count()
                    data10= Grade.objects.filter(subject='数据库原理', grade__gte=90).count()


                    data_1={'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5}
                    data_2 = {'data6': data6, 'data7': data7, 'data8': data8, 'data9': data9, 'data10': data10}

                    context = {'teacher':teacher,'paper':paper,'data_1':data_1,'data_2':data_2}
                    return render(request,'exam/teacherLogin.html', context=context)
                
                message = '密码不正确！' 
            except :
                message = '教师不存在！'                

    login_form = TeacherForm()
    return render(request, 'exam/loginTeacher.html', locals())

#教师查看成绩
def showGrade(request):
    subject1=request.GET.get('subject')
    grade=Grade.objects.filter(subject=subject1)

    data1 = Grade.objects.filter(subject=subject1, grade__lt=60).count()
    data2 = Grade.objects.filter(subject=subject1, grade__gte=60, grade__lt=70).count()
    data3 = Grade.objects.filter(subject=subject1, grade__gte=70, grade__lt=80).count()
    data4 = Grade.objects.filter(subject=subject1, grade__gte=80, grade__lt=90).count()
    data5 = Grade.objects.filter(subject=subject1, grade__gte=90).count()

    data = {'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5}

    return render(request,'showGrade.html',{'grade':grade,'data':data,'subject':subject1})

#教师按条件查询学生
def queryStudent(request):
    #获取教师查询的条件值
    sid=request.GET.get('id')
    sex=request.GET.get('sex')
    subject=request.GET.get('subject')

    #获取老师的id
    tid=request.GET.get('tid')
    teacher = Teacher.objects.get(id=tid)
    paper = Paper.objects.filter(tid=teacher.id)

    # print(sid,sex,subject)
    from django.db import connection,transaction
    cursor=connection.cursor()
    sql="select * from grade,student where student.id=grade.sid_id " \
        "and student.id like %s and grade.subject like %s and student.sex like %s and '1'='1'"
    val=('%'+sid+'%','%'+subject+'%','%'+sex+'%')
    cursor.execute(sql,val)
    result=dictfetchall(cursor)


    # print(result)
    return render(request,'teacher.html',{'teacher':teacher,'result':result,'paper':paper})

#将使用原生sql语句查到的结果由tuple类型转换为dictionary(字典)类型
def dictfetchall(cursor):
    "将游标返回的结果保存到一个字典对象中"
    desc = cursor.description
    return [
    dict(zip([col[0] for col in desc], row))
    for row in cursor.fetchall()
    ]


#学生考试 的视图函数
def startExam(request):
    sid = request.GET.get('sid')
    pid = request.GET.get('pid')

    student=Student.objects.get(id=sid)
    # 当前试卷
    # paper=Paper.objects.filter(id=pid)
    paper=Paper.objects.get(id=pid)
    # 学生和考试试卷 exam.html
    return render(request,'exam/exam.html',{'student':student,'paper':paper})


#计算由exam.html模版传过来的数据计算成绩
def calGrade(request):

    if request.method=='POST':
        # 学号和试卷号
        sid=request.POST.get('sid')
        pid = request.POST.get('pid')

        # 重新生成Student实例，Paper实例，Grade实例，名字和index中for的一致，可重复渲染
        student= Student.objects.get(id=sid)
        # 当前测试试卷
        paper = Paper.objects.get(id=pid)
        # grade = Grade.objects.filter(sid=student.id)

        # 计算该门考试的学生成绩 
        question= paper.qid.values('id','answer','score')

        score=0   # 初始化一个成绩为0
        for q in question:
            qid=str(q['id'])            # int 转 string,通过qid找到题号
            ans=request.POST.get(qid) # 通过 qid 得到学生关于该题的作答  

            if ans==q['answer']:#判断学生作答与正确答案是否一致
                score+=q['score']#若一致,得到该题的分数,累加score变量

        #向Grade表中插入数据
        Grade.objects.create(sid_id=sid,subject=paper.subject,grade=score)
        grade = Grade.objects.filter(sid=student.id)
        # 有关该生的所有试卷
        paper=Paper.objects.filter(major=student.major)
        # 重新渲染studentLogin.html模板
        return render(request,'exam/studentLogin.html',{'student':student,'paper':paper,'grade':grade})










