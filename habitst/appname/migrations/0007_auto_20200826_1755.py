# Generated by Django 2.2 on 2020-08-26 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0006_auto_20200825_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
    ]
