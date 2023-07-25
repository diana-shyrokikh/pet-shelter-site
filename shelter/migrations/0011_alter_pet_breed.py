# Generated by Django 4.2.3 on 2023-07-21 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("shelter", "0010_alter_breed_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="breed",
            field=models.ForeignKey(
                blank=True,
                default="unknown",
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="pets_breed",
                to="shelter.breed",
            ),
        ),
    ]
