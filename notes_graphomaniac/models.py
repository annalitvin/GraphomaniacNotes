from django.db import models


# Create your models here.

class Note(models.Model):
    text = models.TextField(max_length=900, verbose_name="Как дела?")
    count_unique_words = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Дата {0}".format(self.date)

    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"
