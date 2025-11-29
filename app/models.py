from pydantic import BaseModel
from typing import List, Optional


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    question: str
    user_id: Optional[str] = None
    history: Optional[List[ChatMessage]] = None


class SourceMeta(BaseModel):
    return_name: str
    sheet_name: str
    line_code: str
    line_desc: str


class ChatResponse(BaseModel):
    answer: str
    sources: List[SourceMeta]
    raw_metadata: Optional[List[dict]] = None

