# Generated by Django 5.0.6 on 2024-07-02 02:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rental", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="temp_cultural_facilities",
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
                ("name", models.CharField(max_length=255)),
                ("loc", models.CharField(max_length=255)),
                ("category", models.CharField(max_length=255)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("rate", models.FloatField(default=0.0)),
                ("address", models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name="rentalstation",
            name="loc",
            field=models.CharField(default="Unknown Location", max_length=255),
        ),
    ]
