# Generated by Django 2.0.1 on 2020-02-19 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TOrder',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 't_order',
                'managed': False,
            },
        ),
    ]