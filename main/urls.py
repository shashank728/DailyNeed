from django.urls import path

from django.conf.urls.static import static
from django.conf import settings


from .import views


urlpatterns = [
    path("",views.home,name="home"),
    path("todo",views.todo,name="todo"),
    path('addtodo/',views.addtodo,name="addtodo"),
    
    path('profile/',views.profile,name="profile"),
    
    path('profile_form/<int:info_id>',views.profile_form,name="profile_form"),
    path('delete_todo/<int:todo_id>',views.delete,name="delete"),
    path('update_todo/<int:todo_id>',views.update,name="update"),
    path('complete/<int:todo_id>',views.complete,name="complete"),
    
]+ static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

