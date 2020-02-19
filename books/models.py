from django.db import models

class Book(models.Model):

    title = models.CharField("Title", max_length=50)
    author = models.ForeignKey("Author", verbose_name="Author", on_delete=models.CASCADE)
    publisher = models.ForeignKey("Publisher", verbose_name="Publisher", on_delete=models.CASCADE)
    language = models.CharField("Language", max_length=50)
    pages = models.DecimalField("Pages", max_digits=5, decimal_places=2)
    created_at = models.DateTimeField("Created at", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})




class Author(models.Model):

    name = models.CharField('Author', max_length=50)
    nationality = models.CharField('Nationality', max_length=50)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})




class Publisher(models.Model):

    name = models.CharField('Name', max_length=50)
    cowntry = models.CharField('Cowntry', max_length=50)

    class Meta:
        verbose_name = "Publisher"
        verbose_name_plural = "Publishers"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    


    