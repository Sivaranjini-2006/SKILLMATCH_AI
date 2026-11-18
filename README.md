# SKILLMATCH AI

**An intelligent skill-based career recommendation system**

SKILLMATCH AI is a Python and Streamlit web application prototype. Students enter their qualification and skills, and the application compares those skills with a predefined dataset of 10 job roles.

## Features

- Student profile and skill input
- Dataset of 10 predefined job roles
- Skill-based matching percentage
- Top 3 recommended job roles
- Match percentage chart
- Matched and missing skill analysis
- Improvement suggestions
- Downloadable CSV recommendation report

## Technology stack

- Python
- Streamlit
- Pandas
- CSV dataset

## Project structure

```text
SKILLMATCH_AI/
├── app.py
├── requirements.txt
├── README.md
├── database/
│   └── job_roles.csv
└── modules/
    ├── __init__.py
    └── recommendation.py
```

## Setup on Windows (VS Code)

1. Install Python 3.10 or newer.
2. Open this folder in VS Code.
3. Open Terminal > New Terminal.
4. Run the following commands:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

If PowerShell blocks environment activation, run this once in the same terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

If activation is not possible, you can install and run using the virtual environment directly:

```powershell
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe -m streamlit run app.py
```

The application normally opens at `http://localhost:8501`.

## How matching works

For each job role:

`Match percentage = (Number of matched required skills / Total required skills) * 100`

The app compares skill names without case sensitivity, ranks the job roles by match percentage, and displays the top three. Career interests are used only as a small tie-breaker when ranking.

## Important project limitation

This is a rule-based recommendation prototype using a curated CSV dataset. It does not train a machine-learning model, fetch live job vacancies, or guarantee employment. The recommendations depend on the skills and job requirements present in the dataset.
