from django.urls import path
from app1 import views
app_name='app1'

urlpatterns = [
    path('',views.index,name='index'),
    path('base/',views.base,name='base'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')

]
