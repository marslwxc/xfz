# Generated by Django 2.0 on 2020-02-14 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xfzauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]
