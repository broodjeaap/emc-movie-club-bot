# Generated by Django 4.2.15 on 2024-08-16 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0011_telegramgroup_uuid"),
    ]

    operations = [
        migrations.AddField(
            model_name="inpersonmoviesuggestion",
            name="processed",
            field=models.BooleanField(default=False),
        ),
    ]
