# Generated by Django 4.0.3 on 2022-05-25 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stages_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_treatment', models.CharField(max_length=100)),
                ('diagnosis_fin', models.CharField(max_length=100)),
                ('quality_cast', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('conclusion', models.CharField(max_length=100)),
                ('date_record', models.DateField()),
                ('next_date', models.DateField()),
                ('prosthesis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.prosthesis')),
            ],
        ),
    ]
