from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    # Getting the number of quizzes under this Category
    @property  
    # this deco is used for reaching quiz_set()
    # like an attribute: quiz_count 
    def quiz_count(self):
        return self.quiz_set.count()
    

class Quiz(models.Model):
    title = models.CharField(max_length=100, verbose_name='Quiz Title')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Quizzes'
        
    # Getting the number of quizzes under this Category
    @property  
    # this deco is used for reaching quiz_set()
    # like an attribute: quiz_count 
    def question_count(self):
        return self.question_set.count()
    
    
class Question(models.Model):
    SCALE = (
        (0, 'Beginner'),
        (1, 'Intermediate'),
        (2, 'Advenced'),
    )
    
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, verbose_name='question')
    difficulty = models.IntegerField(choices=SCALE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    answer_text = models.CharField(max_length=250)
    is_right = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.answer_text