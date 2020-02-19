# Generated by Django 3.0.3 on 2020-02-27 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_delete_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='nacionality',
            new_name='nationality',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_author', to='books.Author', verbose_name='Author'),
        ),
    ]
