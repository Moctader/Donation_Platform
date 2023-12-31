# Generated by Django 4.2.5 on 2023-09-28 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('post_date', models.DateTimeField()),
                ('is_finished', models.BooleanField(default=False)),
            ],
        ),
    ]
