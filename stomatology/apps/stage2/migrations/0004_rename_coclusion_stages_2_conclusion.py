# Generated by Django 4.0.3 on 2022-05-31 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stage2', '0003_alter_stages_2_date_record_alter_stages_2_next_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stages_2',
            old_name='coclusion',
            new_name='conclusion',
        ),
    ]