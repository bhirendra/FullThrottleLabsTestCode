"""FullThrottleLabsCode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from users.apis import api_users_list, api_reset_users
from django.views.defaults import page_not_found

schema_view = get_schema_view(
    openapi.Info(
        title="Full Throttle Labs Code",
        default_version='v1',
        description="This documentation contains all the API used in this project",
        contact=openapi.Contact(email="bhirendra2014@gmail.com")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),

)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Swagger API documetation urls (First url is for normal layout, another one is for modern layout)
    path('api/doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/uidoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # API URL of getting users list
    path('api/users-list/', api_users_list, name="api-users-list"),
    # API URL of reset users data from DB
    path('api/reset-users/', api_reset_users, name="api-reset-users"),
]
# Throw 404 for other unacceptable urls
urlpatterns += url(r'^.*$', page_not_found, {'exception': Exception('Not Found')}),
