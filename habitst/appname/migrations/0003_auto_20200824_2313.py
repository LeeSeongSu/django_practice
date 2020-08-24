# Generated by Django 3.1 on 2020-08-24 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0002_auto_20200813_2103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='상품명')),
                ('desc', models.TextField(blank=True)),
                ('amount', models.PositiveIntegerField(verbose_name='결제금액')),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]