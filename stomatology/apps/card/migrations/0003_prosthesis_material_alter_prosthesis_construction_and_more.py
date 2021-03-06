# Generated by Django 4.0.3 on 2022-05-31 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_construction_type_prost'),
        ('card', '0002_alter_patientcard_client_alter_prosthesis_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='prosthesis',
            name='material',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.materials'),
        ),
        migrations.AlterField(
            model_name='prosthesis',
            name='construction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.construction'),
        ),
        migrations.AlterField(
            model_name='prosthesis',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.type_prost'),
        ),
    ]
