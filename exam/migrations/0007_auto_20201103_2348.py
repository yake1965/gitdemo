# Generated by Django 3.1.2 on 2020-11-03 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_auto_20201101_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[('2', 'general'), ('3', 'difficult'), ('1', 'easy')], default='1', max_length=32, verbose_name='等级'),
        ),
    ]
