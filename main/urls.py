from django.urls import path
from django.conf.urls import url
from . import views
app_name = "main"
urlpatterns = [
    path('',views.index,name= 'index'),
    path('addtodo/',views.add_to_do, name= 'addtodo'),
    path('search/',views.search, name= 'search'),
    path('deletetodo/<int:iddelete>',views.delete_to_do, name= 'deletetodo'),
    path('deletelist/<int:idlist>',views.delete_list, name= 'deletelist'),
    path('completetodo/<int:idcomplete>',views.complete_to_do, name= 'completetodo'),
    path('undo/<int:idundo>',views.undo_to_do, name= 'undo'),
    path('edit/<int:idedit>',views.edit_to_do, name= 'edit'),
    path('indexSpecificTask/<int:idSpecificTask>',views.indexSpecificTask, name= 'indexSpecificTask'), 
    path('addlist/',views.add_list, name= 'addlist'),
]
 