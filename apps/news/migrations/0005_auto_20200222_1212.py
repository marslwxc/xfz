# Generated by Django 2.0 on 2020-02-22 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_banner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'ordering': ['priority']},
        ),
    ]