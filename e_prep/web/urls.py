from django.urls import path, include

from e_prep.web.views import index, delete_album, delete_profile, add_album, edit_album, details_profile, details_album


urlpatterns = (
    path('', index, name='index'),
    path('album/', include([
        path('details/<int:pk>/', details_album, name='details album'),
        path('add/', add_album, name='add album'),
        path('edit/<int:pk>/', edit_album, name='edit album'),
        path('delete/<int:pk>/', delete_album, name='delete album'),
    ])),
    path('profile/', include([
        path('details/', delete_profile, name='details album'),
        path('delete/', details_profile, name='delete album'),
    ])),
)
