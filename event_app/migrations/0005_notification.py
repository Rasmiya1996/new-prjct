# Generated by Django 4.2.7 on 2023-12-15 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("event_app", "0004_rename_club_event_club_1"),
    ]

    operations = [
        migrations.CreateModel(
            name="Notification",
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
                ("date", models.DateField()),
                ("description", models.CharField(max_length=50)),
            ],
        ),
    ]
