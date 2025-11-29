from fastapi import FastAPI
from app.models import ChatRequest, ChatResponse, SourceMeta
from app.services.rag_service import rag_pipeline

app = FastAPI(title="Bank GPT Backend")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    answer, metadata_list = rag_pipeline.query(req.question, req.history)

    sources = [
        SourceMeta(
            return_name=m.get("return", ""),
            sheet_name=m.get("sheet", ""),
            line_code=str(m.get("line_code", "")),
            line_desc=m.get("line_desc", "")
        )
        for m in metadata_list
    ]

    return ChatResponse(
        answer=answer,
        sources=sources,
        raw_metadata=metadata_list
    )
