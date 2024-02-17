# Generated by Django 4.2.7 on 2024-02-08 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("event_app", "0008_join_request"),
    ]

    operations = [
        migrations.CreateModel(
            name="Join",
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
                ("status", models.IntegerField(default=0)),
                (
                    "approve",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="event_app.join_request",
                    ),
                ),
                (
                    "user_2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="event_app.student",
                    ),
                ),
            ],
        ),
    ]