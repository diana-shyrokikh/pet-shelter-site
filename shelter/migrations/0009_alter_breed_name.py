# Generated by Django 4.2.3 on 2023-07-21 17:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shelter", "0008_alter_type_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="breed",
            name="name",
            field=models.CharField(
                default="Unknown",
                max_length=255,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="The value must consist of A-z and a-z only",
                        regex="^[A-Za-z]+$",
                    )
                ],
            ),
        ),
    ]
