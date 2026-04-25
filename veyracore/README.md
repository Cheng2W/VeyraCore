# VeyraCore / 灵枢

AI Service Orchestration Platform - AI 服务编排平台

## Quick Start

```bash
# Copy environment file
cp .env.example .env

# Start all services
docker compose up --build
```

## Architecture

- **Backend**: FastAPI + SQLAlchemy (Async) + Celery
- **Frontend**: Next.js 14 + React 18 + TailwindCSS + Zustand
- **Database**: PostgreSQL 16
- **Cache/Queue**: Redis 7
- **Task Queue**: Celery Workers

## Services

| Service | Port | Description |
|---------|------|-------------|
| Frontend | 3000 | Next.js Application |
| Backend | 8000 | FastAPI REST API |
| PostgreSQL | 5432 | Database |
| Redis | 6379 | Cache & Message Broker |

## AI Services Supported (25 placeholders)

1. KeLing (可灵)
2. Tongyi Wanxiang (通义万相)
3. JiMeng (即梦)
4. OpenAI
5. Anthropic
6. Google Gemini
7. Midjourney
8. Stable Diffusion
9. DALL-E
10. Cohere
11. Hugging Face
12. Replicate
13. Runway ML
14. Pika Labs
15. ElevenLabs
16. AssemblyAI
17. Deepgram
18. Azure OpenAI
19. Baidu Wenxin (文心一言)
20. Tencent Hunyuan (腾讯混元)
21. iFlytek Spark (讯飞星火)
22. Zhipu AI (智谱)
23. Moonshot AI (月之暗面)
24. MiniMax
25. SenseTime (商汤)

## Development

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## License

MIT
