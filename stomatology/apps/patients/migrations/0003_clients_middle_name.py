# Generated by Django 4.0.3 on 2022-06-12 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_alter_clients_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='middle_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]