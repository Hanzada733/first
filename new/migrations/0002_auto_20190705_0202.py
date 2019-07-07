# Generated by Django 2.2.3 on 2019-07-04 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='new.Brands'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='marketing',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='new.Marketing'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='sait',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='new.Saits'),
            preserve_default=False,
        ),
    ]