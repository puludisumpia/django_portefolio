# Generated by Django 3.2.3 on 2021-05-16 15:26

from django.db import migrations, models
import fontawesome_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='VOTRE NOM')),
                ('email', models.EmailField(max_length=100, verbose_name='VOTRE MAIL')),
                ('content', models.TextField(verbose_name='VOTRE MESSAGE')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='images/portefolio/')),
                ('note', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('modal_id', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Technologie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', fontawesome_5.fields.IconField(blank=True, max_length=60)),
                ('note', models.TextField()),
            ],
        ),
    ]
