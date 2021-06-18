# Generated by Django 3.0.6 on 2020-05-30 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Who_we_are',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Titles')),
                ('des', models.TextField(verbose_name='Description')),
                ('is_verified', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'WHO_WE_ARE',
                'verbose_name_plural': 'WHO_WE_ARE',
                'ordering': ['-id'],
            },
        ),
    ]
