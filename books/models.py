from django.db import models

class Book(models.Model):

    title = models.CharField("Title", max_length=50)
    author = models.CharField("Author", max_length=50)
    publisher = models.CharField("Publisher", max_length=50)
    language = models.CharField("Language", max_length=50)
    pages = models.DecimalField("Pages", max_digits=5, decimal_places=2)
    reviews = models.CharField("Reviews", max_length=50)
    created_at = models.DateTimeField("Created at", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

