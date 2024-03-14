# Generated by Django 5.0.3 on 2024-03-13 18:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
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
                ("customer_id", models.IntegerField()),
                ("account_number", models.IntegerField()),
                (
                    "balance",
                    models.DecimalField(decimal_places=2, default="0", max_digits=5),
                ),
                ("deposit", models.DecimalField(decimal_places=2, max_digits=5)),
                ("withdraw", models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]