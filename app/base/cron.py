from django_cron import CronJobBase, Schedule
from .models import Quiz
from django.utils import timezone

class UpdateQuizStatusCronJob(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'your_app_name.update_quiz_statuses'  # Replace 'your_app_name' with the actual name of your app

    def do(self):
        current_time = timezone.now()
        quizzes_to_activate = Quiz.objects.filter(start_date__lte=current_time, end_date__gte=current_time)
        quizzes_to_activate.update(status='active')

        quizzes_to_finish = Quiz.objects.filter(end_date__lt=current_time + timezone.timedelta(minutes=5))
        quizzes_to_finish.update(status='finished')