# Generated by Django 4.2.7 on 2023-12-03 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyResponse',
            fields=[
                ('participant_id', models.AutoField(primary_key=True, serialize=False)),
                ('q1', models.IntegerField(verbose_name='How satisfied are you with the overall quality of the course content?')),
                ('q2', models.IntegerField(verbose_name='The instructor effectively communicated the course material.')),
                ('q3', models.IntegerField(verbose_name='The assignments and assessments were clear and relevant.')),
                ('q4', models.IntegerField(verbose_name='The pace of the course was appropriate.')),
                ('q5', models.IntegerField(verbose_name='The course materials (slides, readings, etc.) were helpful.')),
                ('q6', models.IntegerField(verbose_name='The instructor was approachable and responsive to questions.')),
                ('q7', models.IntegerField(verbose_name='The feedback provided on assignments was constructive.')),
                ('q8', models.IntegerField(verbose_name='The technology used in the course (if applicable) was reliable.')),
                ('q9', models.IntegerField(verbose_name='How likely are you to recommend this course to others?')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Additional comments or suggestions')),
            ],
            options={
                'verbose_name': 'Survey Response',
                'verbose_name_plural': 'Survey Responses',
            },
        ),
    ]
