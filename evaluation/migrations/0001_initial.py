# Generated by Django 3.0.14 on 2021-10-11 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('city', models.CharField(blank=True, max_length=120, null=True)),
                ('company', models.CharField(blank=True, max_length=200, null=True)),
                ('expectation', models.CharField(blank=True, max_length=50, null=True)),
                ('courseware', models.CharField(blank=True, max_length=50, null=True)),
                ('instructor_assessment', models.CharField(blank=True, max_length=50, null=True)),
                ('general_evaluation', models.CharField(max_length=50)),
                ('others', models.TextField(blank=True, null=True)),
                ('instructor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='evaluation.Instructor')),
                ('training', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='evaluation.Training')),
            ],
        ),
    ]
