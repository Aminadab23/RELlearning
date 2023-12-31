# Generated by Django 4.2.4 on 2023-08-25 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tyle', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('landingDescription', models.TextField()),
                ('goal', models.TextField()),
                ('languagesQuealified', models.TextField()),
                ('mentorsCallMessage', models.TextField()),
                ('exploreEthiopiaText', models.TextField()),
                ('sudentsNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_type', models.CharField(max_length=100)),
                ('pricePerYear', models.CharField(max_length=10)),
                ('generalDescription', models.TextField()),
                ('detailDescription', models.TextField()),
            ],
            options={
                'verbose_name': 'Package',
                'verbose_name_plural': 'Packages',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('certification', models.BooleanField(default=False)),
                ('expectedTrainee', models.CharField(max_length=60)),
                ('price', models.CharField(max_length=10)),
                ('duration', models.CharField(max_length=12)),
                ('noOfLessons', models.IntegerField()),
                ('noOfQuizes', models.IntegerField()),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrators.languages')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('price', models.CharField(max_length=10)),
                ('numberOfPages', models.IntegerField()),
                ('file', models.FileField(upload_to='books/')),
                ('iconImage', models.ImageField(upload_to='bookIcon/')),
                ('rating', models.CharField(max_length=10)),
                ('uploadDate', models.DateField(auto_now_add=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrators.booktype')),
            ],
        ),
    ]
