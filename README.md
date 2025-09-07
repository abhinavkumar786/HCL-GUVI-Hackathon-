AI_RESUME_Reviewer:

AI Resume Reviewer is a frontend Streamlit application that provides AI-powered instant feedback on resumes. It evaluates content quality, formatting, ATS compatibility, and keywords, and generates actionable recommendations to optimize resumes for target roles.

Supports PDF uploads and text input, with optional job description analysis for more precise feedback.

Features:

1. Upload resume (PDF) or paste text

2. AI analysis using OpenAI GPT-4, Claude, or Google Gemini

3. Select Job Role, Industry, and Experience Level

4. Shows overall score, content quality, ATS score, and grade

5. Highlights strengths and weaknesses with recommendations

6. Section-by-section detailed analysis

7. Export results: PDF report, JSON data, or copyable summary

8. Demo mode to test with sample resumes and job descriptions

9. Privacy-focused: data processed in real-time, not stored

How to Run:

1. Clone the repository:

git clone https://github.com/your-username/ai-resume-reviewer.git
cd ai-resume-reviewer


2. Install dependencies:

pip install -r requirements.txt


3. Run the app:

streamlit run app.py


4. Open the URL in your browser (http://localhost:8501).

Usage:

1. Configure AI Provider, Job Role, Industry, and Experience Level in the sidebar.

2. Upload a PDF resume or paste resume text.

3. Optionally, add a job description for targeted feedback.

4. Set advanced analysis options if desired.

5. Click “Analyze My Resume” to get feedback.

6. View strengths, weaknesses, scores, and recommendations in tabs.

7. Export results as PDF, JSON, or copy summary.

8. Use demo mode to try with sample resumes.

