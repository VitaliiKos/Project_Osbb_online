from django_filters import rest_framework as filters

from apps.readings.models import MeterReadingsModel


class MeterReadingFilter(filters.FilterSet):
    date_gte = filters.DateFilter(field_name='created_at', lookup_expr='gt')
    date_lte = filters.DateFilter(field_name='created_at', lookup_expr='lt')
    date_exact = filters.DateFilter(field_name='created_at', lookup_expr='exact')
