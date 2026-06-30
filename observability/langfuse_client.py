import os
from langfuse import get_client
from langfuse.langchain import CallbackHandler
from config.settings import settings
from utils.logger import get_logger

logger = get_logger("langfuse-client")

_langfuse = None
_langfuse_handler = None


def get_langfuse():
    global _langfuse

    if _langfuse is not None:
        return _langfuse

    os.environ["LANGFUSE_PUBLIC_KEY"] = settings.langfuse_public_key
    os.environ["LANGFUSE_SECRET_KEY"] = settings.langfuse_secret_key
    os.environ["LANGFUSE_BASE_URL"] = settings.langfuse_base_url

    _langfuse = get_client()

    if _langfuse.auth_check():
        logger.info("Langfuse client is authenticated")
    else:
        logger.error("Authentication failed. Check credentials")

    return _langfuse


def get_langfuse_handler():
    global _langfuse_handler

    if _langfuse_handler is None:
        _langfuse_handler = CallbackHandler()

    return _langfuse_handler