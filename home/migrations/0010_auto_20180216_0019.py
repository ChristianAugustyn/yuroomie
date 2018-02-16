# Generated by Django 2.0.2 on 2018-02-16 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_merge_20180216_0018'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='room',
            name='visits',
        ),
        migrations.AddField(
            model_name='room',
            name='visists',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='thumbnail',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AddField(
            model_name='roomimage',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Room'),
        ),
    ]
