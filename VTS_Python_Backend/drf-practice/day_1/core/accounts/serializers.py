from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

from .models import Student,Links
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password','email','bio','designation']
 
class LinksSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Links
        fields = "__all__" 

class StudentSerializer(serializers.ModelSerializer):
    links = LinksSerializers(many=True)
    class Meta:
        model = Student
        fields = ["id",'name','age','links']
        
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)

        request = self.context.get("request")
        if request and request.query_params.get("lang") == "bn":
            if "name" in self.fields:
                self.fields["name_bd"] = self.fields.pop("name")


# class StudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length=100)
#     age = serializers.IntegerField()
#     just_check = serializers.SerializerMethodField()
    

#     def validate_age(self,value):
#         if value < 10: 
#             raise serializers.ValidationError("you are a child! go to heal")
#         pass

#     def get_just_check(self,obj):
#         return f"{obj['name']} - {obj['age']}"