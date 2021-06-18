# Generated by Django 3.0.6 on 2020-05-30 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titles')),
                ('des', models.TextField(verbose_name='Description')),
                ('style_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Style Name')),
                ('is_verified', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'ALL SERVICES',
                'verbose_name_plural': 'ALL SERVICES',
                'ordering': ['-id'],
            },
        ),
    ]