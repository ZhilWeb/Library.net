from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('add/add_success/', submit_add_book),
    path('edit/<int:id>/edit_success/', page_edit_book),
    path('delete/<int:id>/', page_delete_book),
    path('add/', page_add_book),
    path("edit/<int:id>/", page_edit_book),
    path("signout/", page_signout),
    path("signup/signup_success/", submit_signup),
    path("signup/", page_signup),
    path("signin/signin_success/", submit_signin),
    path("signin/", page_signin),
    path('limit=<int:limit>/page=<int:page>/', home_page_view_with_params),
    path('', home_page_view, name='home')
]
