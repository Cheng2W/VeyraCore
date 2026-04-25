# VeyraCore - AI Service Orchestration Platform

## Project Structure

```
veyracore/
├── docker-compose.yml          # Docker orchestration
├── .env.example                # Environment variables template
├── README.md                   # Documentation
├── docs/                       # Documentation files
│
├── backend/                    # FastAPI Backend
│   ├── Dockerfile              # Backend container config
│   ├── requirements.txt        # Python dependencies
│   └── app/
│       ├── __init__.py
│       ├── main.py             # FastAPI application entry
│       ├── config.py           # Pydantic settings (25 AI API keys)
│       ├── database.py         # Async SQLAlchemy setup
│       ├── celery_app.py       # Celery configuration
│       └── tasks.py            # Celery tasks
│
└── frontend/                   # Next.js Frontend
    ├── Dockerfile              # Frontend container config
    ├── package.json            # Node dependencies
    ├── next.config.js          # Next.js config (API proxy)
    ├── tailwind.config.js      # TailwindCSS config
    ├── postcss.config.js       # PostCSS config
    ├── tsconfig.json           # TypeScript config
    └── src/
        ├── app/
        │   ├── layout.tsx      # Root layout
        │   ├── page.tsx        # Home page
        │   └── globals.css     # Global styles
        ├── components/
        │   └── Header.tsx      # Header component
        ├── store/
        │   └── useAppStore.ts  # Zustand store
        └── lib/
            └── api.ts          # Axios client
```

## Quick Start

1. Copy `.env.example` to `.env`
2. Run `docker compose up --build`
3. Access:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Health: http://localhost:8000/api/health
