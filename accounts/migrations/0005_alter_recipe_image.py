# Generated by Django 3.2.12 on 2023-03-28 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_gen_ins_recipe_delete_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
