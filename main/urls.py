from django.urls import path
from django.conf.urls import url
from . import views
app_name = "main"
urlpatterns = [
    path('',views.index,name= 'index'),
    path('addtodo/',views.add_to_do, name= 'addtodo'),
    path('deletetodo/<int:iddelete>',views.delete_to_do, name= 'deletetodo'),
    path('completetodo/<int:idcomplete>',views.complete_to_do, name= 'completetodo'),
    path('undo/<int:idundo>',views.undo_to_do, name= 'undo'),
    path('edit/<int:idedit>',views.edit_to_do, name= 'edit'),
]
 