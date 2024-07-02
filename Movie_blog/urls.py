from django.contrib import admin
from django.urls import path
from app_movie import views
from user import views as user_v1

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',views.main_movie_page_view,name='main'),
    path('upload/',views.Upload_img_blog_view,name='upload'),
    path('home/',views.home_page_view,name='home'),
    path('nav/',views.Navigation_page_view,name='nav'),
    path('fulldetails/<int:id>/',views.Full_details_View,name='fulldetails'),
    path('trailer/',views.Trailer_view,name='trailer'),
    path('review/',views.Movie_review_page_view,name='review'),
    path('about/',views.About_page_view,name='about'),
    path('contact/',views.Contact_page_view,name='contect'),
    path('register/',user_v1.Register_form_view,name='register'),
    path('',user_v1.log_in_view,name='login'),
    path('logout/',user_v1.log_out_view,name='logout'),
    path('intro/',views.intro_view,name='intro')
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
