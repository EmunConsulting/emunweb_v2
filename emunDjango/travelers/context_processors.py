# context_processors.py
from travelers.models import ProfileImage


def user_profile_image(request):
    if request.user.is_authenticated:
        try:
            profile_image = ProfileImage.objects.get(user=request.user)
        except ProfileImage.DoesNotExist:
            profile_image = None
        return {'profile_image': profile_image}
    return {}
