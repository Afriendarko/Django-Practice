# Generated by Django 3.0.3 on 2020-02-26 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_auto_20200226_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, unique=True)),
                ('Artist_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='demoapp.Musician1')),
            ],
        ),
    ]
