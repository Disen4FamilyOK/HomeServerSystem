# Generated by Django 2.0.1 on 2020-02-19 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TAppuser',
            fields=[
                ('user_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='用户ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='用户名')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='手机号')),
            ],
            options={
                'verbose_name': '会员管理',
                'verbose_name_plural': '会员管理',
                'db_table': 't_appuser',
                'managed': False,
            },
        ),
    ]
