from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Profile(models.Model):
    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=255, help_text='e.g. "GenAI Developer · CSE-AIML · Builder"')
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=200, default="Nellore, AP, India")
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    logo = models.ImageField(upload_to='profile/', blank=True, null=True)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    university = models.CharField(max_length=200, blank=True, null=True)
    degree = models.CharField(max_length=200, blank=True, null=True)
    available_for_hire = models.BooleanField(default=True)
    years_experience = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
    
    def __str__(self):
        return self.name

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('GenAI/LLM', 'GenAI/LLM'),
        ('Machine Learning', 'Machine Learning'),
        ('Deep Learning', 'Deep Learning'),
        ('Backend', 'Backend'),
        ('Frontend', 'Frontend'),
        ('DevOps', 'DevOps'),
        ('Database', 'Database'),
        ('Tools', 'Tools'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    icon_class = models.CharField(max_length=50, help_text='Font Awesome class string, e.g., "fa-brands fa-python"')
    highlight = models.BooleanField(default=False, help_text='Show as featured skill badge in hero')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return f"{self.name} ({self.category})"

class Project(models.Model):
    STATUS_CHOICES = [
        ('Completed', 'Completed'),
        ('Ongoing', 'Ongoing'),
        ('In Progress', 'In Progress'),
    ]
    CATEGORY_CHOICES = [
        ('GenAI', 'GenAI'),
        ('ML/DL', 'ML/DL'),
        ('Full Stack', 'Full Stack'),
        ('API', 'API'),
        ('Computer Vision', 'Computer Vision'),
        ('Other', 'Other'),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    tagline = models.CharField(max_length=255)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255, help_text='Comma-separated values')
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='projects/', blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Completed')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Full Stack')
    is_featured = models.BooleanField(default=False)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-start_date']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

class Experience(models.Model):
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    employment_type = models.CharField(max_length=50, help_text='e.g., Hybrid/Remote/Virtual Internship')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    location = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    tech_tags = models.CharField(max_length=255)
    company_logo = models.ImageField(upload_to='companies/', blank=True, null=True)

    class Meta:
        ordering = ['-start_date']
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"

    def __str__(self):
        return f"{self.role} at {self.company}"

class Education(models.Model):
    SCORE_TYPE_CHOICES = [
        ('CGPA', 'CGPA'),
        ('Percentage', 'Percentage'),
    ]
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field = models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)
    score = models.CharField(max_length=20, blank=True, null=True)
    score_type = models.CharField(max_length=20, choices=SCORE_TYPE_CHOICES, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-start_year']
        verbose_name = "Education"
        verbose_name_plural = "Educations"

    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    issued_date = models.DateField()
    credential_url = models.URLField(blank=True, null=True)
    badge_image = models.ImageField(upload_to='certifications/', blank=True, null=True)

    class Meta:
        ordering = ['-issued_date']
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"

    def __str__(self):
        return self.name

class Achievement(models.Model):
    CATEGORY_CHOICES = [
        ('Hackathon', 'Hackathon'),
        ('Exam', 'Exam'),
        ('Event', 'Event'),
        ('Award', 'Award'),
    ]
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    rank_or_result = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['-date']
        verbose_name = "Achievement"
        verbose_name_plural = "Achievements"

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-sent_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

class TechStack(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    logo_url = models.CharField(max_length=255, help_text='External CDN logo URL or icon class')
    color_hex = models.CharField(max_length=7, help_text='e.g., #FFFFFF', blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Tech Stack Item"
        verbose_name_plural = "Tech Stack Items"

    def __str__(self):
        return self.name
