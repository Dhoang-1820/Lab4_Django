from rest_framework import serializers
from weather_web.weather.models import Sensordata


class SensordataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensordata
        fields = ('id',
                  'humidity',
                  'temperature',
                  'time')