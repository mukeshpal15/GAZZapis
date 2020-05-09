
from rest_framework import serializers
from testapp.models import useres
'''
class UsersignupSerializer(serializers.ModelSerializer):
	class Meta:
		model = useres
		fields = ('Full_Name','phone_no','email','password')

class userLoginSerializer(serializers.ModelSerializer):
	class Meta:
		model = useres
		fields= ('email', 'password')

class Userforgotpassword(serializers.ModelSerializer):
	class Meta:
		model = useres
		fields= ('password',)
class UpdateUserdetails(serializers.ModelSerializer):
	class Meta:
		model = useres
		fields= '__all__'
'''
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.response import Response

class UseresSerializer(serializers.ModelSerializer):

    class Meta:
        model = useres
        fields = (
            'Full_Name',
            'email',
            'phone_no',
            'password',
            
        )
        def save(self):

        	useres = useres(
        		Full_Name=self.validated_data['Full_Name'],
        		email=self.validated_data['email'],
        		phone_no=self.validated_data['phone_no'],
        		password=self.validated_data['password'],
        		)
        	useres.save()
        	data['response']="Successful"
        	return Response(data)

class ForgotPasswordUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = useres
		fields= ('email','password',)

class userLoginSerializer(serializers.ModelSerializer):
	class Meta:
		model = useres
		fields= ('email', 'password',)