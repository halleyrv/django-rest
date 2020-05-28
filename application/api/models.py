from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=70)

    class Meta:
        db_table = "hr_person"

    def __str__(self):
        return self.name


class Task(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=70)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = "hr_task"

    def __str__(self):
        return self.name