from django.urls import path
from .views import ProfileList, ProfileDetail

app_name = 'profiles'

urlpatterns = [
    path('', ProfileList.as_view(), name='list'),
    path('<username>/', ProfileDetail.as_view(), name='detail'),

]

