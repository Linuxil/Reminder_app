# Generated by Django 3.2 on 2024-02-19 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(choices=[('Monday ', 'Monday '), ('Tuesday', 'Tuesday'), ('Wednesday ', 'Wednesday '), ('Thursday ', 'Thursday '), ('Friday ', 'Friday '), ('Saturday ', 'Saturday '), ('Sunday ', 'Sunday ')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('surname', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('telegram', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Out_of_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('employee', models.ManyToManyField(blank=True, to='main.Employees')),
                ('position', models.ManyToManyField(blank=True, to='main.Positions')),
                ('template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.messages')),
            ],
        ),
        migrations.CreateModel(
            name='Message_rass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=5)),
                ('day_of_week', models.ManyToManyField(blank=True, to='main.Day')),
                ('employee', models.ManyToManyField(blank=True, to='main.Employees')),
                ('position', models.ManyToManyField(blank=True, to='main.Positions')),
                ('template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.messages')),
            ],
            options={
                'verbose_name_plural': 'Schedule_messages',
            },
        ),
        migrations.AddField(
            model_name='employees',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.positions'),
        ),
    ]
