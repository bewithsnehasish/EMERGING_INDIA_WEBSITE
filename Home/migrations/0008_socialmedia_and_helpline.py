# Generated by Django 5.0.6 on 2024-07-24 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_rename_organiztion_team_member_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia_and_HelpLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, max_length=255, null=True)),
                ('twitter', models.URLField(blank=True, max_length=255, null=True)),
                ('linkedin', models.URLField(blank=True, max_length=255, null=True)),
                ('instagram', models.URLField(blank=True, max_length=255, null=True)),
                ('youtube', models.URLField(blank=True, max_length=255, null=True)),
                ('helpline_no', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Social Media Links',
                'verbose_name_plural': 'Social Media Links',
            },
        ),
    ]