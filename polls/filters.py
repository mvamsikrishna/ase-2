from .models import Question
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Question
        fields = ['question_text', ]
