# Generated by Django 5.0.6 on 2024-09-09 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0008_arogya_form_cancer_awareness_form_clean_india_form_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer_form',
            name='Aadhar_no',
            field=models.CharField(max_length=200),
        ),
    ]