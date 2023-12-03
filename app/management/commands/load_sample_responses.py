# app_name/management/commands/load_survey_responses.py
import csv
from django.core.management.base import BaseCommand
from app.models import SurveyResponse

class Command(BaseCommand):
    help = 'Load survey responses from CSV file'

    def handle(self, *args, **options):
        file_path = '/home/naveen/projects/django/FeedbackInsight/data.csv'  # Replace with the actual path to your CSV file

        with open(file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                SurveyResponse.objects.create(
                    participant_id=row['Participant ID'],
                    q1=row['Q1'],
                    q2=row['Q2'],
                    q3=row['Q3'],
                    q4=row['Q4'],
                    q5=row['Q5'],
                    q6=row['Q6'],
                    q7=row['Q7'],
                    q8=row['Q8'],
                    q9=row['Q9'],
                    comments=row['Comments']
                )

        self.stdout.write(self.style.SUCCESS('Survey responses loaded successfully'))
