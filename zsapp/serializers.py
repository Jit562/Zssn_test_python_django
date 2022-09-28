from rest_framework import serializers

from .models import *

class LocationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Location

        fields = "__all__"
        
        


class SurvivorSerializer(serializers.ModelSerializer):

    locations = LocationSerializer(many=True, read_only =True)

    class Meta:

        model = Survivor

        fields = ['id','created_at','updated_at','name','age','gender','locations']


        def create(self, validated_data):
            location = validated_data.pop('locations')
            location_instance = Survivor.objects.create(**validated_data)
            for loc in location:
                loc.objects.create(user=location_instance,**loc)
            return location_instance
        

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.age = validated_data.get('age', instance.age)
            instance.gender = validated_data.get('gender', instance.gender)
            instance.locations.lat = validated_data.get('lat', instance.locations.lat)
            instance.locations.long = validated_data.get('long', instance.locations.long)
            instance.save()
            return instance