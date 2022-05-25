# Generated by Django 4.0.3 on 2022-05-25 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('producer', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('availability', models.IntegerField()),
                ('quality', models.IntegerField()),
            ],
        ),
    ]
