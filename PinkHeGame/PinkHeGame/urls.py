"""PinkHeGame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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


#from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('arrangement_time_format/', include('arrangement_time_format.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns = [
    path('to_test/', include('to_test.urls')),
    path('admin/', admin.site.urls),
]

# urlpatterns = [
#     path('hello/', testhe.hello),
# ]
# urlpatterns = [
#     url(r'^$', testhe.hello),
# ]

