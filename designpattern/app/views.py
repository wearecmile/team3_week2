from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializer import *
from rest_framework.response import Response
from utils import *
from rest_framework import status
# Create your views here.


def custom_response(status='',  data={}, message='',  is_pagination=False, is_error=True, errors={}):
    if not is_pagination:
        return Response({"is_error": is_error, 'result': data, 'message': message}, status=status)
    return Response({"is_error": is_error, **data, 'message': message}, status=status)

class ADDCARAPI(GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = CarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return custom_response(is_error=False,message=CAR_BRAND_ADDED_SUCCESSFULLY,status=status.HTTP_200_OK)
        else:
            return custom_response(is_error=True,message=PLEASE_ENTER_VALID_DATA,status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request,id=None):
        if id:
            try:
                data = Car.objects.get(id=id)
            except Car.DoesNotExist:
                return custom_response(is_error=True,message=CAR_BRAND_DOES_NOT_EXISTS,status=status.HTTP_400_BAD_REQUEST)

            serializers =  CarSerializer(data).data
            return custom_response(is_error=False,data=serializers,message=CAR_BRAND_DETAILS,status=status.HTTP_200_OK)
        all_car_data = Car.objects.all().order_by('-id')
        serializers =  CarSerializer(all_car_data,many=True).data
        
        return custom_response(is_error=False,data=serializers,message=CAR_BRAND_DETAILS,status=status.HTTP_200_OK)

       
    
        
class CarModelSDetailAPI(GenericAPIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,car_model_id):
        try:
            data = CarModel.objects.get(car_model_id=car_model_id)
        except CarModel.DoesNotExist:
            return custom_response(is_error=True,message=CAR_MODEL_DOES_NOT_EXISTS,status=status.HTTP_200_OK)

        serializer = CarModelSerializer(data).data
        return custom_response(is_error=False,data=serializer,message=CAR_MODEL_DETAILS_MESSAGE,status=status.HTTP_200_OK)

    def delete(self,request,car_model_id):
        try:
            data = CarModel.objects.get(car_model_id=car_model_id).delete()
        except CarModel.DoesNotExist:
            return custom_response(is_error=True,message=CAR_MODEL_DOES_NOT_EXISTS,status=status.HTTP_200_OK)

        return custom_response(is_error=False,message=CAR_MODEL_DELETED_SUCCESSFULLY,status=status.HTTP_200_OK)





class CarBrandModelDETAILS(GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,id):
        try:
            car_object = Car.objects.get(id=id)
        except Car.DoesNotExist:
            return custom_response(is_error=True,message=CAR_BRAND_DOES_NOT_EXISTS,status=status.HTTP_400_BAD_REQUEST)
        
        filtered_car_models = CarModel.objects.filter(car_id=car_object)
        serializer = CarModelSerializer(filtered_car_models,many=True).data
        return custom_response(is_error=False,data=serializer,message=CAR_MODEL_DETAILS_MESSAGE,status=status.HTTP_200_OK)

