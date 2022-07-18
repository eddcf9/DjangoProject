# Generated by Django 4.0.5 on 2022-07-18 19:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_author_book_bookinstance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('summary', models.TextField(help_text='De que trata la pelicula', max_length=100)),
                ('isbn', models.CharField(help_text='El isbn es de 13 caracteres', max_length=13, verbose_name='ISBN')),
            ],
        ),
        migrations.CreateModel(
            name='MovieInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='id unico para este libro', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On Load'), ('a', 'Available'), ('r', 'Reserved')], default='m', help_text='Disponibilidad de la pelicula', max_length=1)),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.movie')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='book',
        ),
        migrations.RenameModel(
            old_name='Author',
            new_name='Director',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='BookInstance',
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.director'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(to='catalog.genero'),
        ),
    ]