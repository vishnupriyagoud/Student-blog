from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UsersViewSet)
router.register('blog', views.BlogViewSet)
router.register('admins', views.AdminsViewSet)
router.register('comments', views.CommentsViewSet)



"""urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

"""
urlpatterns = [
    path('', views.index1, name='index1'),
    #path('/', include(router.urls)),
    re_path('finduser/', views.finduser, name='finduser'),
    path('post/<pk>', views.post_delete, name='post_delete'),
    path('edit/<pk>', views.post_edit, name='post_edit'),
    path('edit_db/<pk>', views.edit_post, name='edit_post'),
    path('report/<pk>', views.post_report, name='post_report'),
    path('block/<pk>', views.post_block, name='post_block'),
    path('stats/', views.stats, name='stats'),
    path('<slug:slug>/', views.post_comment, name='post_comment'),
    
]