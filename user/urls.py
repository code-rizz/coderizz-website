from django.urls import path,include
from django.conf.urls.static import static
from user.views import *
from django.conf import settings

urlpatterns = [
    path("",dashboard, name="dashboard"),
    path("projects",project, name="projects"),
    path("projects/delete/<int:id>",del_project),
    path("projects/add",add_project),
    path("content_library",content_library, name = "content_library"),
    path("content",content, name = "content"),
    path("users/<email>",users, name="users"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)