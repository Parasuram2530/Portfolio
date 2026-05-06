from django.contrib import admin
from .models import (
    Profile, Skill, Project, Experience, 
    Education, Certification, Achievement, 
    ContactMessage, TechStack
)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline', 'email', 'available_for_hire')
    search_fields = ('name', 'email', 'tagline')
    list_filter = ('available_for_hire',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'highlight', 'order')
    search_fields = ('name', 'category')
    list_filter = ('category', 'highlight')
    list_editable = ('proficiency', 'highlight', 'order')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'is_featured', 'order')
    search_fields = ('title', 'tagline', 'description', 'tech_stack')
    list_filter = ('category', 'status', 'is_featured')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('status', 'is_featured', 'order')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'employment_type', 'start_date', 'is_current')
    search_fields = ('role', 'company', 'tech_tags')
    list_filter = ('employment_type', 'is_current')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_year', 'end_year', 'score')
    search_fields = ('institution', 'degree', 'field')
    list_filter = ('score_type',)

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuer', 'issued_date')
    search_fields = ('name', 'issuer')
    list_filter = ('issued_date',)

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'category', 'date')
    search_fields = ('title', 'organization')
    list_filter = ('category',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'sent_at', 'is_read')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('is_read', 'sent_at')
    readonly_fields = ('sent_at',)

@admin.register(TechStack)
class TechStackAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'order')
    search_fields = ('name', 'category')
    list_filter = ('category',)
    list_editable = ('order',)
