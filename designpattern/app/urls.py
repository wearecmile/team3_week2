from django.urls import path
from .views import *

urlpatterns = [
    # User authentication API #14
    path('add-cars-brand/', ADDCARAPI.as_view(),
         name='add-cars-brand/'),

    path('get-car-brand-details/<int:id>/',ADDCARAPI.as_view()),
     path('get-car-brand-details/',ADDCARAPI.as_view()),
    path('get-car-model-details/<str:car_model_id>/',CarModelSDetailAPI.as_view()),
    path('get-car-model-detail-by-brand-name/<int:id>/',CarBrandModelDETAILS.as_view())

]