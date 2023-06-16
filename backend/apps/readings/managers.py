from django.db.models import QuerySet


class MeterReadingsManager(QuerySet):
    def get_readings_by_meter_id(self, id):
        return self.filter(meter_id=id)


class StandardMeterPymentManager(QuerySet):
    def get_standard_payments_by_standard_meter_type_id(self, id):
        return self.filter(standard_meter_type_id=id)
