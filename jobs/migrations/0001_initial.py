# Generated by Django 5.1.1 on 2024-10-06 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Job",
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
                ("title", models.CharField(max_length=100)),
                ("company", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("location", models.CharField(max_length=100)),
                (
                    "employment_type",
                    models.CharField(
                        choices=[
                            ("Full-time", "Full-time"),
                            ("Part-time", "Part-time"),
                            ("Contract", "Contract"),
                        ],
                        max_length=50,
                    ),
                ),
                ("posted_on", models.DateField(auto_now_add=True)),
                ("application_deadline", models.DateField()),
            ],
        ),
    ]
