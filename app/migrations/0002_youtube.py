# Generated by Django 3.2.12 on 2022-02-15 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='URL')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.song')),
            ],
        ),
    ]
