# Generated by Django 5.0.6 on 2024-08-05 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_alter_socialmedia_and_helpline_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='footer_and_home_page_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('people_got_clothes', models.IntegerField()),
                ('handicaps_got_help', models.IntegerField()),
                ('people_got_medical_help', models.IntegerField()),
            ],
        ),
    ]