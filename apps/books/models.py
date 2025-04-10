from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"



class Book(models.Model):
    title = models.CharField(max_length=100)
    pages = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.title