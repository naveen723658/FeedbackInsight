# app_name/forms.py
from django import forms


class FeedbackSurveyForm(forms.Form):
    participant_id = forms.CharField(label="Unique UserID",widget=forms.TextInput(attrs={"class": "form-control"}),  required=True)

    # Define Likert scale choices
    LIKERT_CHOICES = [
        ("1", "1 - Strongly Disagree"),
        ("2", "2 - Disagree"),
        ("3", "3 - Neutral"),
        ("4", "4 - Agree"),
        ("5", "5 - Strongly Agree"),
    ]

    questions = [
        "How satisfied are you with the overall quality of the course content?",
        "The instructor effectively communicated the course material.",
        "The assignments and assessments were clear and relevant.",
        "The pace of the course was appropriate.",
        "The course materials (slides, readings, etc.) were helpful.",
        "The instructor was approachable and responsive to questions.",
        "The feedback provided on assignments was constructive.",
        "The technology used in the course (if applicable) was reliable.",
        "How likely are you to recommend this course to others?",
    ]

    for i, question in enumerate(questions, start=1):
        locals()[f"question_{i}"] = forms.ChoiceField(
            label=question,
            choices=LIKERT_CHOICES,
            widget=forms.RadioSelect(attrs={"class": "form-check-input"}),
            required=True
        )

    comments = forms.CharField(
        label="Do you have any additional comments or suggestions for improvement? (Optional)",
        widget=forms.Textarea(attrs={"class": "form-control"}),
        required=False,
    )
