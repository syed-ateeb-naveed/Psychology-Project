from django.contrib import admin
from .models import Profile,Category,Question,Choice,Result,Questionwithparts,Partsofquestion
# Register your models here.

admin.site.register(Profile)
# Register your models here.
@admin.register(Category)
@admin.register(Question)
@admin.register(Choice)
@admin.register(Questionwithparts)
@admin.register(Partsofquestion)

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