import httpx
from loguru import logger

from app.config import settings, ensure_dirs


def check_ollama() -> bool:
    url = f"{settings.ollama_base_url}/api/tags"
    try:
        response = httpx.get(url, timeout=5.0)
        response.raise_for_status()
        data = response.json()
        models = [m.get("name", "") for m in data.get("models", [])]

        logger.info("Ollama is available. Models: {}", models)

        if not any(m.startswith(settings.llm_model) for m in models):
            logger.warning(
                "LLM model '{}' not found. Run: ollama pull {}",
                settings.llm_model,
                settings.llm_model,
            )

        if not any(m.startswith(settings.embedding_model) for m in models):
            logger.warning(
                "Embedding model '{}' not found. Run: ollama pull {}",
                settings.embedding_model,
                settings.embedding_model,
            )

        return True
    except Exception as exc:
        logger.error("Ollama is unavailable: {}", exc)
        return False


if __name__ == "__main__":
    ensure_dirs()
    logger.info("Запуск {}", settings.app_name)
    logger.info("Папка данных: {}", settings.data_dir)
    check_ollama()