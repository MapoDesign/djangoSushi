# Generated by Django 4.0.4 on 2022-05-11 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('immagine', models.ImageField(upload_to='')),
                ('nome', models.CharField(max_length=20)),
                ('prezzo', models.IntegerField()),
            ],
        ),
    ]