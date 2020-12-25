from django.contrib import admin
from .models import Student,Teacher,Paper,Question,Grade

admin.site.site_header = '考试系统后台'
admin.site.site_title = '考试系统'

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','gender','dept','major','password','email','telephone','birth')# 要显示哪些信息
    list_display_links = ('id','name')#点击哪些信息可以进入编辑页面
    search_fields = ['name','dept','major','birth']   #指定要搜索的字段，将会出现一个搜索框让管理员搜索关键词
    list_filter =['name','dept','major','birth']#指定列表过滤器，右边将会出现一个快捷的过滤选项

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'dept', 'password', 'email','telephone', 'birth')
    list_display_links = ('id', 'name')
    search_fields = ['name', 'dept', 'birth']
    list_filter = ['name','dept']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','subject','title','optionA','optionB','optionC','optionD','answer','level','score')


@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = ('id','tid','major','subject','examtime')
    list_display_links = ('major','subject','examtime')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('sid','subject','grade',)
    list_display_links = ('sid','subject','grade',)
    # fk_fields = ['sid']
