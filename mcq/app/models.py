from django.db import models
from autoslug import AutoSlugField
from account.models import User
from django.db.models.signals import pre_save,pre_delete
from django.dispatch import receiver


class Slider(models.Model):
    image = models.ImageField(upload_to='sliderimage/')
    text = models.CharField(max_length=150, null=True, blank=True)
    order_number = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"
        ordering =['order_number']

    def __str__(self):
        return str(self.image.name)

class Categories(models.Model):
    categories_name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='categoriesimage/')
    order_number = models.IntegerField()
    previous_price = models.IntegerField(null=True, blank=True)
    current_price = models.IntegerField()
    short_descriptions = models.TextField()
    categories_slug = AutoSlugField(populate_from='categories_name', unique=True, default=None)

    class Meta:
        verbose_name = "Question Bank"
        verbose_name_plural = "Question Bank's"
        ordering = ['-order_number']

    def __str__(self):
        return self.categories_name



@receiver(pre_delete, sender=Categories)
def prevent_category_deletion(sender, instance, **kwargs):
    if instance.question_sets.exists():
        raise models.ProtectedError(
            "Cannot delete this category because it has related question sets.",
            models.SET_NULL  
        )

payment_status =(
    ('paid','Paid'),
    ('pending','Pending')
)


class QuestionSets(models.Model):
    categorie = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='question_sets')
    set_name = models.CharField(max_length=300)
    order_number = models.IntegerField()
    is_free = models.BooleanField()
    questions_set_slug = AutoSlugField(populate_from='set_name', unique=True, default=None)

    
    class Meta:
        verbose_name = "Question Set"
        verbose_name_plural = "Question Sets"
        ordering = ['order_number']

    def __str__(self):
        return self.set_name

class Questions(models.Model):
    set_name = models.ForeignKey(QuestionSets, on_delete=models.CASCADE, related_name='question_set_name')
    question = models.CharField(max_length=300)
    file = models.ImageField(upload_to='file/',null=True, blank=True)
    question_slug = AutoSlugField(populate_from='question', unique=True, default=None)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ['-id']

    def __str__(self):
        return self.question

class Answer(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='answers')
    answer = models.CharField(max_length=255)
    answerfile = models.ImageField(upload_to='answerimage/', null=True, blank=True)
    correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"

    def __str__(self):
        return self.answer


class PaymentPatner(models.Model):
    name = models.CharField(max_length=150)
    qr_code = models.ImageField(upload_to='qr/')

    class Meta:
        ordering =['-id']

    def __str__(self):
        return self.name
    

class Purchases(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    sets = models.ForeignKey(QuestionSets, on_delete=models.CASCADE, related_name='questionset')
    payment_status = models.CharField(choices=payment_status, max_length=200, default='pending')
    payment_method = models.ForeignKey(PaymentPatner,on_delete=models.CASCADE, db_constraint=False, related_name='payment_method')
    payment_slip = models.ImageField(upload_to='paymentslip/')
    paid_amount = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Purchase Question Set"
        verbose_name_plural = "Purchases Question Sets"
        ordering=['-id']

    def __str__(self):
        return f"{self.user.name} - {self.sets.set_name} ({self.payment_status})"



# score record
class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_score')
    marks = models.PositiveIntegerField()
    attempt_date= models.DateField(auto_now_add=True)
    

    class Meta:
        verbose_name = "Score"
        verbose_name_plural ="Scores"

    def __str__(self):
        return self.user.name + str(self.marks)

   
