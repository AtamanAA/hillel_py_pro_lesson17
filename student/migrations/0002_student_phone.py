# Generated by Django 4.2 on 2023-05-03 21:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("student", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="phone",
            field=models.CharField(max_length=20, null=True),
        ),
    ]
