# Generated by Django 4.1.6 on 2023-02-04 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mail_track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_email', models.EmailField(max_length=254)),
                ('receiver_email', models.EmailField(max_length=254)),
                ('counter', models.IntegerField(default=0)),
                ('is_opened', models.BooleanField(default=False)),
            ],
        ),
    ]
