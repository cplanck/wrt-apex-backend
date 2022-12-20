# View file specifically for APEX frontend (React) endpoints. 

from django.shortcuts import render
from api.serializers import *
from rest_framework.response import Response
from rest_framework import viewsets, status, permissions
from django.http import HttpResponse, HttpResponseRedirect
from api.models import *
from .helper_functions import *
import json

class APEX_DEPLOYMENTS(viewsets.ViewSet):

	"""
	Viewset for returning list of APEX deployments. 
	Returns either all deployments or a single deployment if a query param is specified.
	
	"""

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
	As of 12/20/2022, 5:40PM: not sure how to evaluate if this is working. 
	Need to plot lat/longs to get a better idea of the data. 
	
	"""
	def list(self, request):
		apex_deployment = self.request.query_params.get('deployment')

		if apex_deployment:
			data = APEX_RAW_DATA.objects.filter(deployment__id=apex_deployment).order_by('gps_hhmmss')
			serializer = APEX_RAW_DATA_Serializer(data, many=True)

			# calculate statistical values to return:
			# distance swept over entire deployment
			meters_traveled, total_time = apex_area_swept(json.dumps(serializer.data))

			return(Response({'meters_traveled' : meters_traveled, 'total_time': total_time}))
		
		else:
			return(Response('no stats...'))

class APEX_DEPLOYMENT_SITES(viewsets.ViewSet):

	"""
	Viewset for returning a JSON of the Deployment Sites and associated APEX machines.
	This view is similar to APEX_DEPLOYMENTS, but it doesn't care if post_data_to_database == False.
	It returns a dictionary of every deployment site with a list of associated APEX machines as keys. 
	"""

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



# user authentication

# BONUS. A search endpoint for returning APEX deployments given a set of search criteria. 