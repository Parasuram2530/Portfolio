import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parasuram_portfolio.settings')
django.setup()

from portfolio.models import Experience, Education, Certification, Achievement

def populate():
    Experience.objects.all().delete()
    Education.objects.all().delete()
    Certification.objects.all().delete()
    Achievement.objects.all().delete()

    # Experience
    Experience.objects.create(
        role="GenAI Developer Intern",
        company="AatonovaZ Technologies",
        employment_type="Hybrid",
        start_date=date(2026, 2, 1),
        is_current=True,
        location="India",
        tech_tags="Gen AI, Python, FastAPI, Antigravity, Kyro AI",
        description="• Built Generative AI APIs using FastAPI for real-time AI-driven applications\n• Developed LLM features using Antigravity and Kyro AI tools\n• Optimized backend performance improving response efficiency"
    )

    Experience.objects.create(
        role="Project Developer Intern",
        company="Infosys",
        employment_type="Virtual",
        start_date=date(2025, 8, 1),
        end_date=date(2025, 9, 30),
        is_current=False,
        tech_tags="Python, LSTM, Machine Learning",
        description="• Developed interactive AQI dashboard visualizing real-time data across multiple locations\n• Built LSTM-based future AQI prediction models\n• Improved model accuracy from 80% → 85% through optimization"
    )

    # Education
    Education.objects.create(
        institution="Mohan Babu University Tirupati",
        degree="B.Tech",
        field="CSE-AIML",
        start_year=2023,
        end_year=2027,
        score="9.42",
        score_type="CGPA",
    )
    Education.objects.create(
        institution="BIEAP Board",
        degree="Senior Secondary",
        field="Science",
        start_year=2021,
        end_year=2023,
        score="96.7",
        score_type="Percentage",
    )
    Education.objects.create(
        institution="SSC Board",
        degree="Secondary (SSC)",
        field="General",
        start_year=2019,
        end_year=2021,
        score="100",
        score_type="Percentage",
    )

    # Certifications
    Certification.objects.create(
        name="ServiceNow Certified System Administrator",
        issuer="ServiceNow",
        issued_date=date(2026, 4, 1),
        credential_url="https://example.com/cert"
    )
    Certification.objects.create(
        name="Google Agentic AI Day — Participation",
        issuer="Google",
        issued_date=date(2025, 7, 1)
    )
    Certification.objects.create(
        name="AWS Cloud Foundations + ML",
        issuer="AICTE Eduskills",
        issued_date=date(2025, 2, 1)
    )
    Certification.objects.create(
        name="Google for Developers",
        issuer="AICTE Eduskills",
        issued_date=date(2025, 6, 1)
    )
    Certification.objects.create(
        name="Edunet Foundation Shell Virtual Internship",
        issuer="Edunet Foundation",
        issued_date=date(2025, 7, 1)
    )

    # Achievements
    Achievement.objects.create(
        title="JEE Mains — 93 percentile",
        organization="NTA",
        date=date(2023, 5, 1),
        category="Exam",
        rank_or_result="93 Percentile",
        description="Scored 93 percentile"
    )
    Achievement.objects.create(
        title="Anna University Hackathon — Pre-final round qualified",
        organization="Anna University",
        date=date(2025, 8, 1),
        category="Hackathon",
        rank_or_result="Pre-finalist",
        description="Qualified for the pre-final round."
    )
    Achievement.objects.create(
        title="Smart India Hackathon — Internal shortlist",
        organization="SIH",
        date=date(2025, 9, 1),
        category="Hackathon",
        rank_or_result="Shortlisted",
        description="Internal shortlist."
    )
    Achievement.objects.create(
        title="Google Agentic AI Day — Ideathon participant",
        organization="Google",
        date=date(2025, 6, 1),
        category="Event",
        rank_or_result="Participant",
        description="Participated in the Ideathon."
    )

    print("Journey populated successfully!")

if __name__ == '__main__':
    populate()
