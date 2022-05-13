# Generated by Django 3.2.8 on 2022-05-06 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('desctiption', models.CharField(max_length=500)),
                ('gravity', models.CharField(max_length=100)),
                ('created_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Mark_x_y',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('Probleme_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marks.mark')),
            ],
        ),
    ]