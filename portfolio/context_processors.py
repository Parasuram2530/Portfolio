from .models import Profile, Certification

def site_data(request):
    return {
        'site_data': {
            'profile': Profile.objects.first(),
            'certifications_count': Certification.objects.count()
        }
    }
