
from django.urls import path
from authapp.views import LoginListView, ProfileCreateView, ProfileUpdateView, Logout

app_name = 'authapp'

urlpatterns = [
    path('login/', LoginListView.as_view(), name='login'),
    path('register/', ProfileCreateView.as_view(), name='register'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('logout/', Logout.as_view(), name='logout'),
]