import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.conf import settings
from .models import (
    Profile, Skill, Project, Experience, 
    Education, Certification, Achievement, 
    ContactMessage, TechStack
)

def index_view(request):
    skills = Skill.objects.all().order_by('order', 'name')
    skills_by_category = {}
    for skill in skills:
        category = skill.category
        if category not in skills_by_category:
            skills_by_category[category] = []
        skills_by_category[category].append(skill)
        
    context = {
        'profile': Profile.objects.first(),
        'skills_by_category': skills_by_category,
        'featured_projects': Project.objects.filter(is_featured=True).order_by('order'),
        'all_projects': Project.objects.all().order_by('order'),
        'experiences': Experience.objects.all().order_by('-start_date'),
        'education': Education.objects.all().order_by('-start_year'),
        'certifications': Certification.objects.all().order_by('-issued_date'),
        'achievements': Achievement.objects.all().order_by('-date'),
        'tech_stack': TechStack.objects.all().order_by('order'),
    }
    return render(request, 'portfolio/index.html', context)

@require_POST
def contact_view(request):
    try:
        # Support both JSON payload and standard form data
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            subject = data.get('subject')
            message = data.get('message')
        else:
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            
        if not all([name, email, subject, message]):
            return JsonResponse({'success': False, 'message': 'All fields are required.'}, status=400)
            
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Send Email notification
        try:
            from django.core.mail import EmailMessage
            
            # Prep the body to include sender info at the top
            body_content = f"From: {name} ({email})\n\n{message}"
            
            email_msg = EmailMessage(
                subject=subject,
                body=body_content,
                from_email=settings.EMAIL_HOST_USER,
                to=[settings.CONTACT_EMAIL],
                reply_to=[email],
            )
            email_msg.send(fail_silently=False)
        except Exception as email_err:
            return JsonResponse({'success': False, 'message': f'Email error: {str(email_err)}'}, status=500)

        return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)

def project_detail_view(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {
        'project': project
    }
    return render(request, 'portfolio/project_detail.html', context)
