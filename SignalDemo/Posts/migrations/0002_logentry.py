# Generated by Django 5.1.1 on 2024-09-19 18:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Posts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LogEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.CharField(max_length=255)),
            ],
        ),
    ]
