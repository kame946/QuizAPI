from django.urls import path
from .views import QuizListCreateView, ActiveQuizView, QuizResultView, AllQuizzesView

urlpatterns = [
    path('quizzes/', QuizListCreateView.as_view(), name='quiz-list-create'),
    path('quizzes/active/', ActiveQuizView.as_view(), name='quiz-active'),
    path('quizzes/<int:id>/result/', QuizResultView.as_view(), name='quiz-result'),
    path('quizzes/all/', AllQuizzesView.as_view(), name='quiz-all'),
]
