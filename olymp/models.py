from django.db import models

class Task(models.Model):
    year = models.IntegerField(verbose_name="Год")
    grade = models.CharField(max_length=10, verbose_name="Класс")
    condition = models.TextField(verbose_name="Условие")
    correct_answer = models.CharField(max_length=255, verbose_name="Ответ")
    solution = models.TextField(verbose_name="Решение")

    def __str__(self):
        return f"{self.year} — {self.grade} класс"