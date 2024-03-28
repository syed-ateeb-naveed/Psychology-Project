from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    CIVIL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('relationship', 'In a Relationship'),
    ]
    civil_status = models.CharField(max_length=20, choices=CIVIL_STATUS_CHOICES)
    occupation = models.CharField(max_length=100)
    place_of_residence = models.CharField(max_length=400)
    cellphone = models.BigIntegerField()
    SCHOOL_LEVEL_CHOICES = [
        ('elementary', 'Elementary/junior school'),
        ('high_school', 'High School'),
        ('bachelour', 'Bachelor’s degree'),
        ('master', 'Master'),
    ]
    level_of_school = models.CharField(max_length=20, choices=SCHOOL_LEVEL_CHOICES)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return str(self.name)
class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField()
    def __str__(self):
        return self.text
class Choice(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    points = models.IntegerField()
    def __str__(self):
        return self.text


class Questionwithparts(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField()
    def __str__(self):
        return self.text
class Partsofquestion(models.Model):
    question = models.ForeignKey(Questionwithparts, on_delete=models.CASCADE)
    text = models.TextField()
    def __str__(self):
        return self.text

class Result(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    mental_status = models.CharField(max_length=10000)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.user)

class Home_page(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    text1 = models.TextField(default="none")
    text2 = models.TextField(default="none")
    photo1 = models.ImageField(upload_to='home_photos/')
    photo2 = models.ImageField(upload_to='home_photos/')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Home Page (frontend)"

class how_does_it_work_page(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    class Meta:
        verbose_name_plural = "Cómo funciona Page (frontend)"

class faq(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "FAQ Page (frontend)"

class how_do_you_feel_page(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    link1= models.CharField(max_length=500)
    link2= models.CharField(max_length=500)
    link3= models.CharField(max_length=500)
    link4= models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "¿Cómo te sientes hoy? Page (frontend)"

class about_us_page(models.Model):
    person1_name=models.CharField(max_length=100)
    person1_description= models.TextField()
    photo1 = models.ImageField(upload_to='about_photos/')
    person2_name=models.CharField(max_length=100)
    person2_description= models.TextField()
    photo2 = models.ImageField(upload_to='about_photos/')
    person3_name=models.CharField(max_length=100)
    person3_description= models.TextField()
    photo3 = models.ImageField(upload_to='about_photos/')

    class Meta:
        verbose_name_plural = "About us Page (frontend)"

class result_anxiety_page(models.Model):
    title = models.CharField(max_length=100)
    photo=models.ImageField(upload_to='result_anxiety_photos/')
    link1= models.CharField(max_length=500)
    link2= models.CharField(max_length=500)
    link3= models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "Anxiety Result Page (frontend)"

class result_depression_page(models.Model):
    title = models.CharField(max_length=100)
    photo=models.ImageField(upload_to='result_depression_photos/')
    link1= models.CharField(max_length=500)
    link2= models.CharField(max_length=500)
    link3= models.CharField(max_length=500)
    link4=  models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "Depression Result Page (frontend)"

class result_autostima_page(models.Model):
    title = models.CharField(max_length=100)

    photo=models.ImageField(upload_to='result_autostima_photos/')
    link1= models.CharField(max_length=500)
    link2= models.CharField(max_length=500)
    link3= models.CharField(max_length=500)
    link4=  models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "Autoestima Result Page (frontend)"

class result_oriention_page(models.Model):
    title = models.CharField(max_length=100)
    photo=models.ImageField(upload_to='result_oriention_photos/')


    class Meta:
        verbose_name_plural = "Orientación Result Page (frontend)"

class Anxiety(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    photo=models.ImageField(upload_to='anxiety_photos/')
    Instruction_Text= models.TextField()
    Instruction_option1= models.CharField(max_length=200)
    Instruction_option2= models.CharField(max_length=200)
    Instruction_option3= models.CharField(max_length=200)
    Instruction_option4= models.CharField(max_length=200)
    link1= models.CharField(max_length=500)
    link2= models.CharField(max_length=500)
    link3= models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "Anxiety Page (frontend)"

class Depression(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    photo=models.ImageField(upload_to='depression_photos/')
    Instruction_Text= models.TextField()
    Instruction_option1= models.CharField(max_length=200)
    Instruction_option2= models.CharField(max_length=200)
    Instruction_option3= models.CharField(max_length=200)
    Instruction_option4= models.CharField(max_length=200)
    link1= models.CharField(max_length=500)
    link2= models.CharField(max_length=500)
    link3= models.CharField(max_length=500)
    link4=  models.CharField(max_length=500)
    class Meta:
        verbose_name_plural = "Depression Page (frontend)"

class Autostima(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    photo=models.ImageField(upload_to='autostima_photos/')
    Instruction_Text= models.TextField()
    Instruction_option1= models.CharField(max_length=200)
    Instruction_option2= models.CharField(max_length=200)
    Instruction_option3= models.CharField(max_length=200)
    Instruction_option4= models.CharField(max_length=200)
    link1= models.CharField(max_length=500)
    link2= models.CharField(max_length=500)
    link3= models.CharField(max_length=500)
    link4=  models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "Autoestima Page (frontend)"

class oriention(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    photo=models.ImageField(upload_to='oriention_photos/')
    Instruction_Text= models.TextField()
    Instruction_option1= models.CharField(max_length=200)
    Instruction_option2= models.CharField(max_length=200)
    Instruction_option3= models.CharField(max_length=200)
    Instruction_option4= models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Orientación Vocacional Page (frontend)"

class Anxiety_quiz_page(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    disclaimer= models.TextField()
    class Meta:
        verbose_name_plural = "Anxiety quiz Page (frontend)"

class Depression_quiz_page(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    disclaimer= models.TextField()
    class Meta:
        verbose_name_plural = "Depression quiz Page (frontend)"

class Autostima_quiz_page(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    disclaimer= models.TextField()
    class Meta:
        verbose_name_plural = "Autoestima quiz Page (frontend)"

class Oriention_quiz_page(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    disclaimer= models.TextField()
    class Meta:
        verbose_name_plural = "Orientación quiz Page (frontend)"

class enduser_page(models.Model):
    text=  models.TextField()
    photo=models.ImageField(upload_to='enduser_photos/')

    class Meta:
        verbose_name_plural = "Enduser Page (frontend)"
