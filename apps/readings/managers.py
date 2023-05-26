from django.db.models import QuerySet


class MeterReadingsManager(QuerySet):
    def get_readings_by_meter_id(self, id):
        return self.filter(meter_id=id)
