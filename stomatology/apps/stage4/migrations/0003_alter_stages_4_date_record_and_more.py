# Generated by Django 4.0.3 on 2022-05-31 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage4', '0002_alter_stages_4_prosthesis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stages_4',
            name='date_record',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='stages_4',
            name='gate_check1',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='stages_4',
            name='gate_check2',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='stages_4',
            name='gate_check3',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='stages_4',
            name='gate_check4',
            field=models.DateField(null=True),
        ),
    ]
