# Generated by Django 2.1.3 on 2018-11-08 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('desc', models.TextField(blank=True)),
                ('catImg', models.FileField(default='catImg/None/default.svg', upload_to='catImg/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityImg', models.ImageField(default='cityImg/None/default.png', height_field='heightField', upload_to='cityImg/', width_field='widthField')),
                ('heightField', models.IntegerField(default=0)),
                ('widthField', models.IntegerField(default=0)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('country', models.CharField(default='india', max_length=120)),
            ],
            options={
                'verbose_name_plural': 'Location',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('designation', models.CharField(max_length=120, unique=True)),
                ('address', models.CharField(max_length=120, unique=True)),
                ('DOB', models.CharField(max_length=120, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('Contact', models.CharField(max_length=14)),
                ('interests', models.CharField(max_length=300)),
                ('profile_pic', models.ImageField(height_field='heightField', upload_to=None, width_field='widthField')),
                ('cover_pic', models.ImageField(height_field='heightField', upload_to=None, width_field='widthField')),
                ('heightField', models.IntegerField(default=0)),
                ('widthField', models.IntegerField(default=0)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='folks.Location')),
            ],
            options={
                'verbose_name_plural': 'Profile',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('desc', models.TextField(blank=True)),
                ('subCatImg', models.FileField(default='subCatImg/None/default.svg', upload_to='subCatImg/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='folks.Category')),
            ],
            options={
                'verbose_name_plural': 'SubCategories',
                'ordering': ('name',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together={('city', 'state')},
        ),
    ]
