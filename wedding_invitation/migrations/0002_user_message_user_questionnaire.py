# Generated by Django 4.0.6 on 2022-07-16 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_invitation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='questionnaire',
            field=models.TextField(null=True),
        ),
    ]
