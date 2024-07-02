# Generated by Django 5.0.6 on 2024-06-13 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie_Blog_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Movie_Title', models.CharField(max_length=30)),
                ('Movie_Release_date', models.DateField()),
                ('Movie_Review_on', models.DateField()),
                ('Movie_Rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('Movie_Trailer', models.TextField()),
                ('Movie_Poster', models.ImageField(upload_to='movies_poster')),
                ('Movie_OneLine_Story', models.TextField()),
                ('Movies_Review', models.TextField()),
            ],
        ),
    ]
