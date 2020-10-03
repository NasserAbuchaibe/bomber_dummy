# Generated by Django 3.1.2 on 2020-10-02 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=60)),
                ('user_name', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('score_project1', models.DecimalField(decimal_places=2, max_digits=4)),
                ('score_project2', models.DecimalField(decimal_places=2, max_digits=4)),
                ('parents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bomber_api.parent')),
            ],
        ),
    ]