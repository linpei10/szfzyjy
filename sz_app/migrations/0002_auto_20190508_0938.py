# Generated by Django 2.1.7 on 2019-05-08 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sz_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='company',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='posotion',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='wechat',
            field=models.CharField(max_length=32, null=True),
        ),
    ]