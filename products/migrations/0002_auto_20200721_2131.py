# Generated by Django 3.0.8 on 2020-07-21 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='recommended_for',
            new_name='recommeded_for',
        ),
    ]
