from django.urls import path, include

from e_prep.web.views import index, delete_album, delete_profile, add_album, edit_album, details_profile, details_album, add_profile


urlpatterns = (
    path('', index, name='index'),
    path('album/', include([
        path('details/<int:pk>/', details_album, name='details album'),
        path('add/', add_album, name='add album'),
        path('edit/<int:pk>/', edit_album, name='edit album'),
        path('delete/<int:pk>/', delete_album, name='delete album'),
    ])),
    path('profile/', include([
        path('add/', add_profile, name='add profile'),
        path('details/', delete_profile, name='details profile'),
        path('delete/', details_profile, name='delete profile'),
    ])),
)
