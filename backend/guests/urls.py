from django.urls import path

from guests.views import IndexView, NewEntryView

urlpatterns = [
    path("", IndexView.as_view(), name="main"),
    path("new", NewEntryView.as_view(), name="add")
]
