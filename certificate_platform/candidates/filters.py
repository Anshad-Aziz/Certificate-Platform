import django_filters
from .models import Candidate

class CandidateFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    course_title = django_filters.CharFilter(lookup_expr='icontains')
    college = django_filters.CharFilter(lookup_expr='icontains')
    start_date = django_filters.DateFilter(field_name='start_date', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='end_date', lookup_expr='lte')

    class Meta:
        model = Candidate
        fields = ['name', 'email', 'course_title', 'college', 'start_date', 'end_date', 'company']
