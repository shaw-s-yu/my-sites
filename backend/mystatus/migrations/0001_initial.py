# Generated by Django 3.0.5 on 2021-01-14 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StatusModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=256, null=True)),
                ('status', models.BooleanField()),
            ],
            options={
                'db_table': 'status',
            },
        ),
    ]