# Generated by Django 2.0.7 on 2019-06-26 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0013_remove_hotels_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='star',
            field=models.CharField(default='1', max_length=10),
            preserve_default=False,
        ),
    ]
