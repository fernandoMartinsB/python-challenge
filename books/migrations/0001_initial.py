# Generated by Django 3.0.3 on 2020-02-18 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('author', models.CharField(max_length=50, verbose_name='Author')),
                ('publisher', models.CharField(max_length=50, verbose_name='Publisher')),
                ('language', models.CharField(max_length=50, verbose_name='Language')),
                ('pages', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Pages')),
                ('reviews', models.CharField(max_length=50, verbose_name='Reviews')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]