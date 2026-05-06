import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parasuram_portfolio.settings')
django.setup()

from portfolio.models import Project

def populate():
    Project.objects.all().delete()
    
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
        category="Machine Learning",
        status="Completed",
        github_url="https://github.com/mannem-parasuram/airaware",
        is_featured=True,
        order=3
    )
    
    print("Projects populated successfully!")

if __name__ == '__main__':
    populate()
