from django.urls import re_path, path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .apis import TodoListApiView, TodoDetailApiView
from django.contrib import admin

# Define the regex pattern for the course ID
COURSE_KEY_PATTERN = r'(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)'
COURSE_ID_PATTERN = COURSE_KEY_PATTERN.replace('course_key_string', 'course_id')

urlpatterns = [
    # URL pattern to match the instructor API endpoint
    # path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path('apis/todos', TodoListApiView.as_view()),
    path('details/todos/<int:todo_id>/', TodoDetailApiView.as_view()),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),

]
