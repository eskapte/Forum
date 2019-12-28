from django.urls import path
from .views import index, DetailPost, UserRegister, UserLogin, user_profile, AddNewPost, DeletePost, ClosePost
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/update', ClosePost.as_view(), name='update'),
    path('<int:pk>/delete', DeletePost.as_view(), name='delete_post'),
    path('<int:pk>', DetailPost.as_view(), name='detail'),
    path('register/', UserRegister.as_view(), name='registration'),
    path('login/', UserLogin.as_view(), name='login'),
    path('profile/<str:username>/', user_profile, name='profile'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('addpost/', AddNewPost.as_view(), name='add_new_post'),

]