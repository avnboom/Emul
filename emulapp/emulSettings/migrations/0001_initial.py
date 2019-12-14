# Generated by Django 3.0 on 2019-12-14 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responseText', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TypeRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=255)),
                ('format_type', models.CharField(choices=[('xml', 'Xml'), ('json', 'Json')], default='XML', max_length=255)),
                ('method_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SearchRules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xpath', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('objectModel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emulSettings.ObjectModel')),
            ],
        ),
        migrations.AddField(
            model_name='objectmodel',
            name='typeRequst',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emulSettings.TypeRequest'),
        ),
    ]
