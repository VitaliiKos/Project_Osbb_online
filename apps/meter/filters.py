from django_filters import rest_framework as filters


class MeterFilter(filters.FilterSet):
    meter_readings_date_lt = filters.DateFilter(field_name='readings', lookup_expr='created_at__lt', distinct=True)
