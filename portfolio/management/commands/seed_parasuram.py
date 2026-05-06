from django.core.management.base import BaseCommand
from portfolio.models import Profile, Skill, Project, Experience, Education, Certification, Achievement, TechStack
from datetime import date

class Command(BaseCommand):
    help = 'Seeds the database with Parasuram\'s portfolio data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        Profile.objects.all().delete()
        Skill.objects.all().delete()
        Project.objects.all().delete()
        Experience.objects.all().delete()
        Education.objects.all().delete()
        Certification.objects.all().delete()
        Achievement.objects.all().delete()
        TechStack.objects.all().delete()

        self.stdout.write('Seeding Profile...')
        Profile.objects.create(
            name="Mannem Parasuram",
            tagline="GenAI Developer · AI/ML Engineer · CSE-AIML @ MBU · Building what's next",
            bio="I am a GenAI Developer and AI/ML Engineer with a deep passion for building scalable, intelligent systems. My expertise spans Python, FastAPI, and leading frameworks like LangChain, HuggingFace, and TensorFlow.\n\nI thrive on architecting solutions that bridge the gap between complex machine learning models and real-world applications. During my internships at AatonovaZ Technologies and Infosys, I deployed robust backend APIs and optimized neural networks to solve critical business problems.\n\nCurrently pursuing my B.Tech in CSE-AIML at Mohan Babu University, I am always exploring emerging technologies, participating in hackathons, and seeking new opportunities to build what's next.",
            email="parasuramgoud30@gmail.com",
            phone="+91-8019666887",
            location="Nellore, Andhra Pradesh, India",
            github_url="https://github.com/mannem-parasuram",
            linkedin_url="https://linkedin.com/in/mannem-parasuram-5410482b8/",
            cgpa=9.42,
            university="Mohan Babu University",
            degree="B.Tech CSE-AIML",
            available_for_hire=True,
            years_experience=1
        )

        self.stdout.write('Seeding Skills...')
        skills_data = [
            ('GenAI/LLM', [
                ('Python', 95, 'fa-brands fa-python', True),
                ('LangChain', 80, 'fa-solid fa-link', True),
                ('HuggingFace', 78, 'fa-solid fa-face-smile', False),
                ('LLMs', 82, 'fa-solid fa-brain', True),
                ('PineCone', 72, 'fa-solid fa-database', False),
                ('Prompt Engineering', 85, 'fa-solid fa-pen-nib', False),
                ('Antigravity', 80, 'fa-solid fa-rocket', False),
                ('Kyro AI', 75, 'fa-solid fa-robot', False)
            ]),
            ('Machine Learning', [
                ('Scikit-Learn', 85, 'fa-solid fa-chart-line', True),
                ('Supervised ML', 88, 'fa-solid fa-project-diagram', False),
                ('Unsupervised ML', 78, 'fa-solid fa-chart-network', False)
            ]),
            ('Deep Learning', [
                ('TensorFlow', 82, 'fa-solid fa-cubes', True),
                ('Keras', 80, 'fa-solid fa-layer-group', False),
                ('PyTorch', 75, 'fa-solid fa-fire', False),
                ('CNNs', 80, 'fa-solid fa-eye', False),
                ('Transformers', 78, 'fa-solid fa-bolt', False),
                ('OpenCV', 82, 'fa-solid fa-camera', False)
            ]),
            ('Backend', [
                ('FastAPI', 88, 'fa-solid fa-server', True),
                ('Django', 80, 'fa-brands fa-python', False),
                ('Flask', 75, 'fa-solid fa-pepper-hot', False),
                ('REST APIs', 85, 'fa-solid fa-network-wired', False)
            ]),
            ('Frontend', [
                ('HTML', 85, 'fa-brands fa-html5', False),
                ('CSS', 82, 'fa-brands fa-css3-alt', False),
                ('JavaScript', 78, 'fa-brands fa-js', False)
            ]),
            ('Database', [
                ('MySQL', 80, 'fa-solid fa-database', False),
                ('MongoDB', 75, 'fa-solid fa-leaf', False)
            ]),
            ('DevOps', [
                ('Docker', 78, 'fa-brands fa-docker', True),
                ('Git', 90, 'fa-brands fa-git-alt', False)
            ]),
            ('Tools', [
                ('VS Code', 90, 'fa-solid fa-code', False),
                ('Postman', 85, 'fa-solid fa-paper-plane', False),
                ('Jupyter', 90, 'fa-solid fa-book-open', False)
            ])
        ]

        order = 1
        for category, category_skills in skills_data:
            for name, proficiency, icon, highlight in category_skills:
                Skill.objects.create(
                    name=name,
                    category=category,
                    proficiency=proficiency,
                    icon_class=icon,
                    highlight=highlight,
                    order=order
                )
                order += 1

        self.stdout.write('Seeding TechStack...')
        techs = ['Python', 'FastAPI', 'Django', 'TensorFlow', 'PyTorch', 'LangChain', 'OpenCV', 'Docker', 'PostgreSQL', 'HuggingFace', 'Gemini', 'Scikit-Learn']
        for i, t in enumerate(techs):
            TechStack.objects.create(name=t, category="Core", logo_url="", order=i)

        self.stdout.write('Seeding Projects...')
        Project.objects.create(
            title="DeepFake Detection System",
            slug="deepfake-detection",
            tagline="AI model classifying deepfake images & videos using FaceForensics++ c40 dataset",
            description="A robust deep learning system designed to detect synthetically generated media and deepfakes. Built using the FaceForensics++ c40 dataset to train the model.",
            tech_stack="Python, Deep Learning, OpenCV, Antigravity, Gemini Flash",
            category="Computer Vision",
            status="Ongoing",
            github_url="https://github.com/mannem-parasuram/deepfake-detector",
            is_featured=True,
            order=1
        )
        Project.objects.create(
            title="AI-Powered Code Review Platform",
            slug="ai-code-review",
            tagline="Live AI code review with WebSocket streaming, GitHub OAuth, and Docker",
            description="A live AI code review platform utilizing WebSockets for real-time streaming feedback from Groq Llama 3.3 70B. Features GitHub OAuth integration and containerized deployment with Docker.",
            tech_stack="FastAPI, WebSockets, PostgreSQL, Docker, Groq Llama 3.3 70B, JWT",
            category="Full Stack",
            status="Completed",
            github_url="https://github.com/mannem-parasuram/ai-code-review",
            live_url="https://ai-code-review.example.com",
            is_featured=True,
            order=2
        )
        Project.objects.create(
            title="AirAware — Air Quality Prediction",
            slug="airaware-prediction",
            tagline="LSTM-based AQI forecasting dashboard across 5 cities, accuracy improved from 80% to 85%",
            description="An intelligent dashboard leveraging LSTM networks to forecast Air Quality Index across 5 major cities. Developed during Infosys internship.",
            tech_stack="Python, LSTM, Scikit-Learn, Streamlit",
            category="ML/DL",
            status="Completed",
            github_url="https://github.com/mannem-parasuram/airaware",
            is_featured=True,
            order=3
        )

        self.stdout.write('Seeding Experience...')
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

        self.stdout.write('Seeding Education...')
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

        self.stdout.write('Seeding Certifications...')
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

        self.stdout.write('Seeding Achievements...')
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

        self.stdout.write(self.style.SUCCESS('Successfully seeded all data!'))
