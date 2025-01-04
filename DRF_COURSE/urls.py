from django.contrib import (
    admin,
)  # Importing the admin module for managing the Django admin site.
from django.urls import (
    path,
    include,
)  # Importing functions to define URL patterns and include other URL configurations.

# Define the root URL patterns for the project.
urlpatterns = [
    path("admin/", admin.site.urls),  # URL for the Django admin interface.
    path("", include("api.urls")),  # Include the URL patterns from the 'api' app.
    path(
        "silk/", include("silk.urls", namespace="silk")
    ),  # Include the URL patterns from the 'silk' app.
]
