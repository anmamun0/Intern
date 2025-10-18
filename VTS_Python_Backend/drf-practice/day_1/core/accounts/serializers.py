from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password','email','bio','designation']
 
 
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()

    def validate_age(self,value):
        if value < 10: 
            raise serializers.ValidationError("you are a child! go to heal")
        pass
    
    def get_just_check(self,obj):
        return f"{obj.bio} - {obj.designation}"