# Generated by Django 4.2 on 2023-06-17 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("teacher", "0004_alter_teacher_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subject",
            name="name",
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="subject",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="teacher.subject",
            ),
        ),
    ]
