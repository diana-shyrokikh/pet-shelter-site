# Generated by Django 4.2.3 on 2023-07-21 15:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shelter", "0004_alter_petowner_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="petowner",
            name="username",
            field=models.CharField(
                max_length=50,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="The username value should consist of a-z, digits and _ only",
                        regex="^[a-z\\d_]+$",
                    )
                ],
            ),
        ),
    ]
