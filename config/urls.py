from django.conrib import admin
from django.urls path, include

urlspatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]