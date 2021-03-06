# Generated by Django 3.0.3 on 2020-02-20 12:18

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20200219_0355'),
    ]

    operations = [

        migrations.RemoveField(
            model_name='book',
            name='reviews',
        ),
        migrations.AddField(
            model_name='review',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='books.Book', verbose_name='Book'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Author', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Publisher', verbose_name='Publisher'),
        ),
    ]
