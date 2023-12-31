# Generated by Django 4.2.3 on 2023-07-21 14:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shelter", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="petowner",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="petowner",
            name="phone_number",
            field=models.CharField(max_length=63, unique=True),
        ),
    ]
