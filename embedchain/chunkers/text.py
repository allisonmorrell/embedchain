from embedchain.chunkers.base_chunker import BaseChunker

from langchain.text_splitter import RecursiveCharacterTextSplitter


TEXT_SPLITTER_CHUNK_PARAMS = {
    "chunk_size": 1000,
    "chunk_overlap": 200,
    "length_function": len,
    "add_start_index": True
}


class TextChunker(BaseChunker):
    def __init__(self):
        text_splitter = RecursiveCharacterTextSplitter(**TEXT_SPLITTER_CHUNK_PARAMS)
        super().__init__(text_splitter)
