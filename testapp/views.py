from django.contrib.auth.models import User
from django.http import Http404
from testapp.models import useres
from testapp.serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, filters
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework import status
from .flutterutils import *
'''
class UserAPIView(generics.ListCreateAPIView):
	search_fields = ['User_Email','User_Password']
	filter_backends = (filters.SearchFilter, )
	queryset = useres.objects.all()
	serializer_class = UsersignupSerializer



import json

@csrf_exempt
def usersLogin(request):
    """
    List all code snippets, or create a new snippet.
  """
    if request.method == 'GET':
        user = useres.objects.all()
        serializer = userLoginSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
    	return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def Userforgotpass(request):
	if request.method=="GET":
		user = useres.objects.all()
		serializer = Userforgotpassword(user, many=True)
		return JsonResponse(serializer.data, safe=False)
	else:
		return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
@csrf_exempt
def modify_in_User_Account(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = useres.objects.get(pk=pk)
    except useres.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserdataSerializer(snippet)
        return JsonResponse(serializer.data)


@csrf_exempt

def update_user_detail(request, pk):

    try:
        snippet = useres.objects.get(pk=pk)
    except useres.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':
    	data = request.data['pk']
    	serializer = UpdateUserdetails(snippet, data=data)
    	data={}
    	if serializer.is_valid():
    		serializer.save()
    		data['success']="Update successfull"
    		return Response(data = data)
    	return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

class UpdateName(generics.UpdateAPIView):
    queryset = useres.objects.all()
    serializer_class = UpdateUserdetails
    def update(request, pk):
	    instance = useres.objects.filter(email=pk)
	    instance.Nickname = request.data.get("Nickname")
	    instance.save()
	    serializer = self.get_serializer(instance)
	    if serializer.is_valid(raise_exception=True):
	    	self.perform_update(serializer)

	    	return Response(serializer.data)'''

@csrf_exempt
@api_view(['POST',])
def Registration(request):
	if request.method == 'POST':

		serializer = UseresSerializer(data=request.data)
		data={}
		dat={}
		if serializer.is_valid():
			serializer.save()
			
			data['Full_Name'] = useres.Full_Name
			data['email'] = useres.email
			data['phone_no'] = useres.phone_no
			data['password'] = useres.password
			dat['response'] = "1"
			return Response(dat)
		else:
			data['response'] = "0"
		return Response(data)

@csrf_exempt
@api_view(['POST',])
def Login(request):
	if request.method == 'POST':

		serializer = userLoginSerializer(data=request.data)
		data={}
		if serializer.is_valid():
			
			data['response'] = "0"
			return Response(data)
		else:
			data['response'] = "1"
			return Response(data)


@api_view(['POST',])
def ForgotPasswordUser(request):
	if request.method=='POST':
		e=request.POST['email']
		data={}
		try:

			instance=useres.objects.filter(pk=e)
			for i in instance:
				e=i.email
				p=i.password
				break
			n=sendmail(e,p)
			if n==1:
				data['Response']='Passwors is send'
				return Response(data)
			else:
				data['Response']='Enter valid email ID'
			return Response(data)

		except:
			data['Response']='Enter valid email ID'
			return Response(data)

