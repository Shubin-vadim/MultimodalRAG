import logging

from langchain.text_splitter import RecursiveCharacterTextSplitter

from backend.core.schemes.config_schemes import ConfigModel


logger = logging.getLogger(__name__)


class DataProcessor:
    """DataProcessor class for handling text tokenization and chunking."""

    def __init__(self, config: ConfigModel) -> None:
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.chunking.chunk_size,
            chunk_overlap=config.chunking.chunk_overlap,
            length_function=len,
            is_separator_regex=False,
            separators=["\n\n", "\n", "\t", ".", "!", "?", ";"],
        )

    def tokenize_texts(self, texts: list[str]) -> list[str]:
        """Tokenize texts into chunks of specified size.

        Args:
            texts: List of text strings to tokenize
        Returns:
            List of tokenized text chunks
        """
        logger.info("Tokenizing %d", len(texts))
        joined_texts = "\n\n".join(texts)
        chunks = self.text_splitter.split_text(joined_texts)
        logger.debug("Tokenized into %d chunks.", len(chunks))
        return chunks
