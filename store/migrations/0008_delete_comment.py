# Generated by Django 4.0.3 on 2022-03-25 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
