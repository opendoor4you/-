from polls.models import Question,Choice

Question.objects.all()

Question.objects.filter(id=1)

Question.objects.filter(question_text__startswith='What')

from django.utils import timezone
current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)





