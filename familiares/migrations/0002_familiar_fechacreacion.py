# Generated by Django 4.1.1 on 2022-10-02 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='fechaCreacion',
            field=models.DateField(null=True),
        ),
    ]
