from django.urls import path
from. import views
# from .views import search_results
urlpatterns = [
    path("",views.index, name="studenthome"),
    path("profileView/<int:myid>",views.profileView,name="profileView"),
    
    path("profileViewList/<int:myid>",views.profileViewList,name="profileViewList"),
    path("search/",views.search_results,name="search"),
    path("search_event/",views.search_event,name="search_event")
    # path("about",views.about, name="about"),
    # path("service",views.service, name="service"),
    

]