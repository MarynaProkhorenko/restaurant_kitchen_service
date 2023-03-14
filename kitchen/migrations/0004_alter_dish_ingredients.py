# Generated by Django 4.1.6 on 2023-03-13 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0003_ingredient_alter_cook_years_of_experience_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='ingredients',
            field=models.ManyToManyField(blank=True, related_name='dishes', to='kitchen.ingredient'),
        ),
    ]
