# Generated by Django 3.0.3 on 2020-02-19 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Author')),
                ('nacionality', models.CharField(max_length=50, verbose_name='Nacionality')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('cowntry', models.CharField(max_length=50, verbose_name='Cowntry')),
            ],
            options={
                'verbose_name': 'Publisher',
                'verbose_name_plural': 'Publishers',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, verbose_name='User')),
                ('rate', models.CharField(max_length=50, verbose_name='Rate')),
                ('feedback', models.TextField(verbose_name='Feedback')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
                'ordering': ['rate'],
            },
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title'], 'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
    ]
