# Generated by Django 2.0.1 on 2020-02-19 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tappuser',
            options={'managed': True, 'verbose_name': '会员管理', 'verbose_name_plural': '会员管理'},
        ),
    ]