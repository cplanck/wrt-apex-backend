from django.shortcuts import render
from api.serializers import *
from rest_framework.response import Response
from rest_framework import viewsets, status, permissions
from api.models import *
import json


class APEX_Data(viewsets.ModelViewSet):

	""" viewset for returning APEX data """

	# permission_classes = [permissions.IsAuthenticated]
	serializer_class = APEX_Data_Serializer
	queryset = APEX_RAW_DATA.objects.all()


class APEX(viewsets.ModelViewSet):

	""" viewset for returning APEX metadata """

	# permission_classes = [permissions.IsAuthenticated]
	serializer_class = APEX_Serializer
	queryset = APEX.objects.all()


class APEX_FILENAMES(viewsets.ViewSet):

	""" 
	Viewset for responding to GET and POST requests
	for APEX datafiles. GET requests responds with "True" or "False" 
	depending on if the filename exists in the database already. POST requests
	add the filename to the DB along with the number of entries written 
	by the dataserver
	"""

	def list(self, request):
		queryset = APEX_RAW_DATA_FILENAMES.objects.all()
		serializer = APEX_RAW_DATA_FILENAMES_Serializer(queryset, many=True)
		return Response(serializer.data)

	def create(self, request):
		# post request should look like {"filename": "APEX015-WRT-121122-SCHIPHOLP4__DAM_000054_2022322_001.dat"}
		filename = request.data['filename']		
		query = APEX_RAW_DATA_FILENAMES.objects.filter(filename=filename)

		if not query:
			# entry doesn't exist, so we should add it (later we should refine to enforce an entries_written field)
			serializer = APEX_RAW_DATA_FILENAMES_Serializer(data={"filename" : filename})
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
		
		else:
			return Response({'entry':'already exists!'})

		return Response({'filename':filename})