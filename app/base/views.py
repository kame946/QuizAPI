from rest_framework import generics, status, throttling
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Quiz
from .serializers import QuizSerializer

class QuizListCreateView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActiveQuizView(APIView):

    def get(self, request):
        active_quiz = Quiz.objects.filter(status='active').first()
        if active_quiz:
            serializer = QuizSerializer(active_quiz)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class QuizResultView(APIView):

    def get(self, request, id):
        quiz = get_object_or_404(Quiz, id=id)
        if quiz.status == 'finished':
            serializer = QuizSerializer(quiz)
            return Response(serializer.data['right_answer'])
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Quiz result not available yet'})

class AllQuizzesView(generics.ListAPIView):

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
