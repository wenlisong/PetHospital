from django.db import models
from Test.models import Test, Question


# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=16)
    name = models.CharField(max_length=30)
    # authority: 0->Intern 1->administrator
    authority = models.IntegerField(default=0)
    user_with_test = models.ManyToManyField(
        Test,
        through='User_test',
        through_fields=('user', 'test'),
    )

    def __str__(self):
        return self.email


class User_test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return 'user{}_test{}'.format(self.user, self.test)


class Usertest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return '{}_{}'.format(self.user, self.test)


class Usertest_question(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    usertest = models.ForeignKey(Usertest, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return '{}_{}'.format(self.usertest, self.question)
