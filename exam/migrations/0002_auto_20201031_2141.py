# Generated by Django 3.1.2 on 2020-10-31 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[('3', 'difficult'), ('1', 'easy'), ('2', 'general')], default='1', max_length=32, verbose_name='等级'),
        ),
    ]
