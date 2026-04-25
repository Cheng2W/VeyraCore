from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

    # Application
    APP_NAME: str = "VeyraCore"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False

    # Database
    DATABASE_URL: str = "postgresql+asyncpg://veyracore:veyracore_secret@localhost:5432/veyracore"

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # CORS
    CORS_ORIGINS: list[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]

    # ============================================
    # AI Service API Keys (25 placeholders)
    # ============================================
    
    # 1. KeLing AI (可灵)
    KELING_API_KEY: Optional[str] = None
    
    # 2. Tongyi Wanxiang (通义万相)
    TONGYI_WANXIANG_API_KEY: Optional[str] = None
    
    # 3. JiMeng AI (即梦)
    JIMENG_API_KEY: Optional[str] = None
    
    # 4. OpenAI
    OPENAI_API_KEY: Optional[str] = None
    
    # 5. Anthropic
    ANTHROPIC_API_KEY: Optional[str] = None
    
    # 6. Google Gemini
    GEMINI_API_KEY: Optional[str] = None
    
    # 7. Midjourney
    MIDJOURNEY_API_KEY: Optional[str] = None
    
    # 8. Stable Diffusion
    STABLE_DIFFUSION_API_KEY: Optional[str] = None
    
    # 9. DALL-E
    DALLE_API_KEY: Optional[str] = None
    
    # 10. Cohere
    COHERE_API_KEY: Optional[str] = None
    
    # 11. Hugging Face
    HUGGINGFACE_API_KEY: Optional[str] = None
    
    # 12. Replicate
    REPLICATE_API_KEY: Optional[str] = None
    
    # 13. Runway ML
    RUNWAY_API_KEY: Optional[str] = None
    
    # 14. Pika Labs
    PIKA_API_KEY: Optional[str] = None
    
    # 15. ElevenLabs
    ELEVENLABS_API_KEY: Optional[str] = None
    
    # 16. AssemblyAI
    ASSEMBLYAI_API_KEY: Optional[str] = None
    
    # 17. Deepgram
    DEEPGRAM_API_KEY: Optional[str] = None
    
    # 18. Azure OpenAI
    AZURE_OPENAI_API_KEY: Optional[str] = None
    
    # 19. Baidu Wenxin (文心一言)
    BAIDU_WENXIN_API_KEY: Optional[str] = None
    
    # 20. Tencent Hunyuan (腾讯混元)
    TENCENT_HUNYUAN_API_KEY: Optional[str] = None
    
    # 21. iFlytek Spark (讯飞星火)
    IFLYTEK_API_KEY: Optional[str] = None
    
    # 22. Zhipu AI (智谱)
    ZHIPU_API_KEY: Optional[str] = None
    
    # 23. Moonshot AI (月之暗面)
    MOONSHOT_API_KEY: Optional[str] = None
    
    # 24. MiniMax
    MINIMAX_API_KEY: Optional[str] = None
    
    # 25. SenseTime (商汤)
    SENSETIME_API_KEY: Optional[str] = None


settings = Settings()
