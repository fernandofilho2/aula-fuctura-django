# Generated by Django 4.2 on 2023-05-02 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='telefone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]