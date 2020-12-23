from django.urls import path
from . import views #import views

urlpatterns = [
    path('', views.manage, name="management"), #root dir
    path('changehours', views.changeHours, name="change_hours"),
    path('settings', views.settings, name="settings"),
    path('staff', views.staff, name="staff"),
    path('update_staff_avail', views.update_staff_avail, name="update_staff_avail"),
    path('remove_staff', views.remove_staff, name="remove_staff"),
    path('view_orders', views.view_orders, name="view_orders"),
    path('<order_number2>', views.order_detail, name="order_detail"),
    path('saveData', views.save_data, name="saveData"),
    path('changeabout', views.changeAbout, name="change_about"),
    path('add_a_product', views.add_a_product, name="add_a_product"),
]
