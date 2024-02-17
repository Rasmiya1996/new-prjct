# Generated by Django 4.2.7 on 2023-12-11 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("event_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Club",
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
                ("club_name", models.CharField(max_length=50)),
                ("image", models.FileField(upload_to="images/")),
                (
                    "staff_incharge",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="event_app.teacher",
                    ),
                ),
            ],
        ),
    ]