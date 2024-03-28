from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Profile)
# Register your models here.
@admin.register(Category)
@admin.register(Question)
@admin.register(Choice)
@admin.register(Questionwithparts)
@admin.register(Partsofquestion)
@admin.register(Home_page)
@admin.register(how_does_it_work_page)
@admin.register(faq)
@admin.register(how_do_you_feel_page)
@admin.register(about_us_page)

@admin.register(Anxiety)
@admin.register(Depression)
@admin.register(Autostima)
@admin.register(oriention)

@admin.register(Anxiety_quiz_page)
@admin.register(Depression_quiz_page)
@admin.register(Autostima_quiz_page)
@admin.register(Oriention_quiz_page)

@admin.register(result_anxiety_page)
@admin.register(result_autostima_page)
@admin.register(result_depression_page)
@admin.register(result_oriention_page)


@admin.register(enduser_page)

class CategoryAdmin(admin.ModelAdmin):
    pass
class QuestionAdmin(admin.ModelAdmin):
    pass
class ChoiceAdmin(admin.ModelAdmin):
    pass
class QuizResultAdmin(admin.ModelAdmin):
    pass

admin.site.register(Result, QuizResultAdmin)

class QuestionwithpartsAdmin(admin.ModelAdmin):
    pass
class PartsofquestionAdmin(admin.ModelAdmin):
    pass
