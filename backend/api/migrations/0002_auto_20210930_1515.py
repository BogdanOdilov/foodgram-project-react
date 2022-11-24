# Generated by Django 3.0.5 on 2021-09-30 12:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['-id'],
                     'verbose_name': 'Ингредиент',
                     'verbose_name_plural': 'Ингредиенты'},
        ),
        migrations.AlterModelOptions(
            name='ingredientamount',
            options={'ordering': ['-id'],
                     'verbose_name': 'Количество ингридиента',
                     'verbose_name_plural': 'Количество ингридиентов'},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-id'],
                     'verbose_name': 'Рецепт',
                     'verbose_name_plural': 'Рецепты'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-id'],
                     'verbose_name': 'Тег',
                     'verbose_name_plural': 'Теги'},
        ),
        migrations.AlterField(
            model_name='ingredientamount',
            name='amount',
            field=models.PositiveSmallIntegerField(
                validators=[django.core.validators.MinValueValidator(
                    1, message='Минимальное количество ингридиентов 1')],
                verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveSmallIntegerField(
                validators=[django.core.validators.MinValueValidator(
                    1, message='Минимальное время приготовления 1 минута')],
                verbose_name='Время приготовления'),
        ),
        migrations.AddConstraint(
            model_name='cart',
            constraint=models.UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique cart user'),
        ),
        migrations.AddConstraint(
            model_name='favorite',
            constraint=models.UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique favorite recipe for user'),
        ),
        migrations.AddConstraint(
            model_name='ingredientamount',
            constraint=models.UniqueConstraint(
                fields=('ingredient', 'recipe'),
                name='unique ingredients recipe'),
        ),
    ]
