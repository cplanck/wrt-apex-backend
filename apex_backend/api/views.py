from django.shortcuts import render
from api.serializers import *
from rest_framework.response import Response
from rest_framework import viewsets, status, permissions
from django.http import HttpResponse, HttpResponseRedirect
from api.models import *
import json


class APEX(viewsets.ModelViewSet):

	""" viewset for returning APEX metadata """

	# permission_classes = [permissions.IsAuthenticated]
	serializer_class = APEX_Serializer
	queryset = APEX.objects.all()


class APEX_FILENAMES(viewsets.ViewSet):

	""" 
	Viewset for responding to GET and POST requests for APEX datafiles. 
	POST requests adds the filename to the DB along with the number of entries written by the dataserver.
	GET requests responds with the names of the files written to the DB

	"""

	def list(self, request):
		queryset = APEX_RAW_DATA_FILENAMES.objects.all()
		serializer = APEX_RAW_DATA_FILENAMES_Serializer(queryset, many=True)
		return Response(serializer.data)

	def create(self, request):
		# post request should look like {"filename": "APEX015-WRT-121122-SCHIPHOLP4__DAM_000054_2022322_001.dat", "entries_written": 121}
		data = request.data
		query = APEX_RAW_DATA_FILENAMES.objects.filter(filename=data['filename'])

		if query and not 'entries_written' in data.keys():
			# entry exists, but no "entries_written" in the body, so we just want to know if there's an entry
			return Response({'entry':'exists!'})
		
		elif not query and not 'entries_written' in data.keys():
			# entry doesn't exists, but there's no entries_written so we'll just respond and not do anything
			return Response({'entry':'not found'})

		elif not query:
			# entry doesn't exist and POST request contains entries_written, so let's add the record to the DB
			serializer = APEX_RAW_DATA_FILENAMES_Serializer(data={"filename" : data['filename'], "entries_written": data['entries_written']})
			if serializer.is_valid():
				serializer.save()
				return Response({'entry':'added!'})
		
		else:
			# entry exists and POST request contains an "entries_written", so lets update entries_written
			query.update(entries_written=data['entries_written'])
			return Response({'success':'entries_written updated!'})


class APEX_DEPLOYMENTS(viewsets.ViewSet):

	"""
	Viewset for returning a JSON of the APEX machines deployed at a given deployment site. Only returns an APEX if post_to_database = True. 
	"""

	def list(self, request):

		deployment_sites_list = list(APEX_DEPLOYMENT.objects.values_list('deployment_site__directory_name').distinct())
		response_list = []

		for deployment_site in deployment_sites_list:
			site_name = deployment_site[0]
			site_apexs = list(APEX_DEPLOYMENT.objects.filter(deployment_site__directory_name=site_name).filter(post_data_to_database=True).values_list('apex__name', flat=True))
			
			if site_apexs:
				response_list.append({site_name:site_apexs})
				print(response_list)
		
		return Response(response_list)


class APEX_RAW_DATA_CRUD(viewsets.ViewSet):

	""" 
	viewset for CRUD on APEX data. Request payload is a list of dictionaries, each 
	defining one sample (lat, long, timestamp, etc.) from an APEX machine.
	
	NOTE 12/19/2022: We should improve this and the data POST routine to be smarter
	so that it runs quicker in production. 
	"""

	def create(self, request):

		data = request.data
		for item in data:
			# add uniqueID to each dictionary (hhmmss + APEX## + DEPLOYMENT_SITE)
			item['uniqueID'] = str(int(item['gps_hhmmss'])*100) + item['apex'].replace(" ", "") + item['deployment_site']
			
			# add associated apex_deployment foreign key
			apex_name = item['apex']
			deployment_site = item['deployment_site']
			apex_deployment = APEX_DEPLOYMENT.objects.filter(apex__name=apex_name).get(deployment_site__directory_name=deployment_site)
			item['deployment'] = apex_deployment.id

			#serialize each item and save it if valid (there isn't already an entry with this uniqueID)
			serializer = APEX_RAW_DATA_Serializer(data=item)
			if serializer.is_valid():
				serializer.save()
				print('SERIALIZER VALID!')

		return Response({'entries added!'})
		
