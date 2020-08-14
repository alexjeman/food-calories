from django.middleware.common import MiddlewareMixin
from apps.users.models import UserAPIKey


class APIKeyAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user_api_key = request.META.get('HTTP_X_API_KEY', None)
        if user_api_key:
            request.user = UserAPIKey.objects.get_from_key(user_api_key).user
