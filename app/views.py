from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FeedbackSurveyForm
from .models import SurveyResponse

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from .models import SurveyResponse
import pandas as pd
import json
def index(request):
    if request.method == "POST":
        form = FeedbackSurveyForm(request.POST)
        if form.is_valid():
            try:
                participant_id = form.cleaned_data["participant_id"]
                q1 = form.cleaned_data["question_1"]
                q2 = form.cleaned_data["question_2"]
                q3 = form.cleaned_data["question_3"]
                q4 = form.cleaned_data["question_4"]
                q5 = form.cleaned_data["question_5"]
                q6 = form.cleaned_data["question_6"]
                q7 = form.cleaned_data["question_7"]
                q8 = form.cleaned_data["question_8"]
                q9 = form.cleaned_data["question_9"]
                comments = form.cleaned_data["comments"]

                # Save the responses to the database
                SurveyResponse.objects.create(
                    participant_id=participant_id,
                    q1=q1,
                    q2=q2,
                    q3=q3,
                    q4=q4,
                    q5=q5,
                    q6=q6,
                    q7=q7,
                    q8=q8,
                    q9=q9,
                    comments=comments,
                )

                messages.success(request, "Thank you for submitting the feedback!")

                return redirect("success")
            except IntegrityError:
                messages.error(
                    request, "Participant ID already exists. Please use a unique ID."
                )
        else:
            # Display form errors
            messages.error(request, "Please correct the errors below.")
    else:
        form = FeedbackSurveyForm()

    return render(request, "index.html", {"form": form})


def success(request):
    return render(request, "success.html")


def result(request):
    # Fetch all survey responses from the database
    responses = SurveyResponse.objects.all()

    # Create a DataFrame from the survey responses
    df = pd.DataFrame(list(responses.values()))

    # Select relevant Likert scale columns for clustering
    likert_columns = [f'q{i}' for i in range(1, 10)]
    data = df[likert_columns]

    # Standardize the data
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)

    # Apply k-means clustering
    kmeans = KMeans(n_clusters=5)  # Adjust the number of clusters as needed
    df['cluster'] = kmeans.fit_predict(data_scaled)
 
    cluster_avg_ratings = df.groupby('cluster')[likert_columns].mean()
    # Calculate average ratings for each cluster
    cluster_avg_ratings_dict = cluster_avg_ratings.to_dict()

    # Pass the clustering results to the template as JSON
    context = {'cluster_avg_ratings': json.dumps(cluster_avg_ratings_dict)}
    return render(request, 'result.html', context)


# def result(request):
#     return HttpDashView.as_view(dash_app)(request)