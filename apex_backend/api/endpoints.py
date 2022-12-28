# View file specifically for APEX frontend (React) endpoints. 

from django.shortcuts import render
from api.serializers import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import viewsets, status, permissions
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.authtoken.models import Token
from api.models import *
from .helper_functions import *
import json

class APEX_DEPLOYMENTS(viewsets.ViewSet):

	"""
	Viewset for returning list of APEX deployments. 
	Returns either all deployments or a single deployment if a query param is specified.
	
	"""

	permission_classes = [IsAuthenticated]

	def list(self, request):
		
		apex_deployment = self.request.query_params.get('deployment')

		if apex_deployment:
			deployments = APEX_DEPLOYMENT.objects.get(id=apex_deployment)
			serializer = APEX_DEPLOYMENT_Serializer(deployments)

		else:
			deployments = APEX_DEPLOYMENT.objects.all()
			serializer = APEX_DEPLOYMENT_Serializer(deployments, many=True)

		return(Response(serializer.data))


# endpoint for returning RAW APEX data. Requires an APEX Deployment as a query param. 
class APEX_RAW_DATA_GIVEN_DEPLOYMENT(viewsets.ViewSet):

	"""
	Viewset for returning a list of dictionaries of raw APEX data. 
	A 'deployment' query parameter is required.
	We will eventually want to add pagination to control the response size here
	
	"""

	permission_classes = [IsAuthenticated]

	def list(self, request):

		apex_deployment = self.request.query_params.get('deployment')

		if apex_deployment:
			data = APEX_RAW_DATA.objects.filter(deployment__id=apex_deployment)
			serializer = APEX_RAW_DATA_Serializer(data, many=True)
			return(Response(serializer.data))

		else:
			return(Response({'error': 'please specify an apex deployment id'}))


	
class APEX_DEPLOYMENT_STATISTICS(viewsets.ViewSet):

	"""
	Viewset for returning a statistics for a given APEX deployment. 
	A 'deployment' query parameter is required.	
	"""

	permission_classes = [IsAuthenticated]

	def list(self, request):
		apex_deployment = self.request.query_params.get('deployment')

		if apex_deployment:
			data = APEX_RAW_DATA.objects.filter(deployment__id=apex_deployment).order_by('gps_hhmmss')
			num_datapoints = data.count()
			print(num_datapoints)
			serializer = APEX_RAW_DATA_Serializer(data, many=True)

			# calculate statistical values to return:
			# distance swept over entire deployment
			meters_traveled, total_time = apex_area_swept(json.dumps(serializer.data))

			return(Response({'meters_traveled' : meters_traveled, 'total_time': total_time, 'num_datapoints': num_datapoints}))
		
		else:
			return(Response('no stats...'))

class APEX_DEPLOYMENT_SITES(viewsets.ViewSet):

	"""
	Viewset for returning a JSON of the Deployment Sites and associated APEX machines.
	This view is similar to APEX_DEPLOYMENTS, but it doesn't care if post_data_to_database == False.
	It returns a dictionary of every deployment site with a list of associated APEX machines as keys. 
	"""

	permission_classes = [IsAuthenticated]

	def list(self, request):

		query = APEX_DEPLOYMENT.objects.all()
		deployment_sites_list = list(DEPLOYMENT_SITE.objects.all().values_list('directory_name'))
		response_list = []

		for deployment_site in deployment_sites_list:
			site_name = deployment_site[0]
			site_apexs = list(query.filter(deployment_site__directory_name=site_name).values_list('apex__name', flat=True))
			
			# if site_apexs:
			response_list.append({site_name:site_apexs})
		
		return Response(response_list)


class DECODE_STATUS(viewsets.ViewSet):

	"""
	Viewset for returning apex deployments that have queue_for_decode == True. Also responds to POST requests for
	toggling queue_for_decode
	"""

	permission_classes = [IsAuthenticated]

	def list(self, request):

		deployments = APEX_DEPLOYMENT.objects.filter(queue_for_decode=True)
		print(deployments)
		serializer = APEX_DECODE_Serializer(deployments, many=True)
		return(Response(serializer.data))

	def create(self, request): 
		try: 
			print(request.data)
			apex = APEX_DEPLOYMENT.objects.filter(id=request.data['apex_id'])
			print(apex)
			apex.update(queue_for_decode=request.data['queue_for_decode'])
			return(Response('Decode queue updated!'))
		
		except:
			return(Response({'There was a problem updating the decode queue'}))


class APEX_USERs(viewsets.ViewSet):

	# def list(self, request):
	# 	print('LIST RAN')
	# 	query = User.objects.all()
	# 	serializer = USER_Serializer(query, many=True)
	# 	return(Response(serializer.data))

	def create(self, request):	
		print('CREATE RAN')

		try: 
			print(request.data)
			user = authenticate(username=request.data['email'], password=request.data['password'])
			if user is not None:
				login(request, user)
			token = Token.objects.get(user_id=user)
			return(Response({'token' : str(token), 'first_name': user.first_name, 'last_name': user.last_name	}))
		except:
			return(Response({'Unable to authenticate user. Please try again.'}))


class LIST_APEX_USERs(viewsets.ViewSet):

	permission_classes = [IsAuthenticated]

	def list(self, request):
		query = User.objects.all().order_by('-last_login')
		serializer = USER_Serializer(query, many=True)
		return(Response(serializer.data))
