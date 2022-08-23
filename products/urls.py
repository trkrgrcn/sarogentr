from django.urls import path
from products import views
from django.conf import settings
from django.conf.urls.static import static

app_name= 'products'

urlpatterns = [
    path('addproduct/', views.addProduct, name='addproduct'),
    path('update/<int:id>', views.updateProduct, name='update'),
    path('delete/<int:id>', views.deleteProduct, name='delete'),
    path('details/<int:id>', views.details, name='details'),
    path('copy/<int:id>', views.copyProduct, name='copy'),
    path('categories/', views.categories, name='categories'),
    ]
