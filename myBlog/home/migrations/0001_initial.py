# Generated by Django 2.0.6 on 2019-04-03 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('title2', models.CharField(default='', max_length=20)),
                ('encode_name', models.CharField(max_length=100)),
                ('encode_a', models.CharField(max_length=100)),
                ('encode_b', models.CharField(max_length=100)),
                ('encode_t', models.CharField(max_length=100)),
                ('key', models.CharField(max_length=50)),
                ('random_text', models.CharField(max_length=120)),
                ('pub_key_byte', models.CharField(max_length=2000)),
                ('pri_key_byte', models.CharField(max_length=2000)),
            ],
        ),
    ]
