# Generated by Django 3.2.8 on 2022-05-15 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0015_auto_20220514_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='mark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points', to='marks.mark'),
        ),
    ]