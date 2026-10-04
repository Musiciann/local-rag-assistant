from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Local RAG Assistant"
    data_dir: Path = Path.home() / ".local_rag_assistant"

    ollama_base_url: str = "http://localhost:11434"
    llm_model: str = "qwen2.5:7b"
    embedding_model: str = "nomic-embed-text"

    chunk_size: int = 400
    chunk_overlap: int = 60
    top_k: int = 5

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    @property
    def db_path(self) -> Path:
        return self.data_dir / "metadata.db"

    @property
    def chroma_dir(self) -> Path:
        return self.data_dir / "chroma"


settings = Settings()


def ensure_dirs() -> None:
    settings.data_dir.mkdir(parents=True, exist_ok=True)
    settings.chroma_dir.mkdir(parents=True, exist_ok=True)