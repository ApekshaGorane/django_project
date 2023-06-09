# Generated by Django 4.1.2 on 2023-02-27 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
                ('author_name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('page', models.IntegerField()),
                ('type_of_book', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'BookModel',
            },
        ),
    ]
