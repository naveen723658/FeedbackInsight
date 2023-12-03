# models.py
from django.db import models

class SurveyResponse(models.Model):
    participant_id = models.AutoField(primary_key=True)
    q1 = models.IntegerField(verbose_name='How satisfied are you with the overall quality of the course content?')
    q2 = models.IntegerField(verbose_name='The instructor effectively communicated the course material.')
    q3 = models.IntegerField(verbose_name='The assignments and assessments were clear and relevant.')
    q4 = models.IntegerField(verbose_name='The pace of the course was appropriate.')
    q5 = models.IntegerField(verbose_name='The course materials (slides, readings, etc.) were helpful.')
    q6 = models.IntegerField(verbose_name='The instructor was approachable and responsive to questions.')
    q7 = models.IntegerField(verbose_name='The feedback provided on assignments was constructive.')
    q8 = models.IntegerField(verbose_name='The technology used in the course (if applicable) was reliable.')
    q9 = models.IntegerField(verbose_name='How likely are you to recommend this course to others?')
    comments = models.TextField(blank=True, null=True, verbose_name='Additional comments or suggestions')
    # cluster = models.IntegerField(null=True)
    def __str__(self):
        return f"Participant {self.participant_id} - {self.q9} / 5"

    class Meta:
        verbose_name = 'Survey Response'
        verbose_name_plural = 'Survey Responses'
