from django.urls import path

from .views import BugListView, BugDetailView, BugCreateView, IndexView


app_name = "bug"
urlpatterns = [
    path("", IndexView.as_view(), name="index"), 
    path("bug_list/", BugListView.as_view(), name="bug_list"),
    path("<int:pk>/", BugDetailView.as_view(), name="bug_detail"),
    path("register/", BugCreateView.as_view(), name="register_bug")
]