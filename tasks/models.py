from django.db import models

class Task(models.Model):
    year = models.IntegerField(verbose_name="Год")
    grade = models.CharField(max_length=10, verbose_name="Класс")
    condition = models.TextField(verbose_name="Условие")
    correct_answer = models.CharField(max_length=255, verbose_name="Ответ")
    solution = models.TextField(verbose_name="Решение")
    image = models.ImageField(
        upload_to='tasks/',
        blank=True,
        null=True,
        verbose_name="Изображение"
    )

    def __str__(self):
        return f"{self.year} — {self.grade} класс"

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class Formula(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    content = models.TextField(verbose_name="Текст (можно HTML)")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")
    year = models.IntegerField(verbose_name="Год")
    grade = models.CharField(max_length=10, verbose_name="Класс")

    class Meta:
        ordering = ['order']
        verbose_name = "Формула"
        verbose_name_plural = "Формулы"

    def __str__(self):
        return f"{self.title} ({self.year} - {self.grade} класс)"
