from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/',views.index,name='dashboard-index'),
    path('staff/',views.staff,name='dashboardstaff'),
    path('staff/details/<int:pk>/',views.staff_details,name='dashboard-staff-details'),
    path('product/',views.product,name='dashboard-product'),
    path('product/delete/<int:pk>/',views.product_delete,name='dashboard-product-delete'),
    path('staff/update/<int:pk>/',views.product_update,name='dashboard-product-update'),
    path('order/',views.order,name='dashboard-order'),

]
