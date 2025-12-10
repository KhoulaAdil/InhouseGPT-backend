from fastapi import FastAPI
from app.models import ChatRequest, ChatResponse, SourceMeta
from app.services.rag_service import rag_pipeline

app = FastAPI(title="Bank GPT Backend")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    print("🔥 /chat endpoint HIT")
    print(f"🔥 User Question: {req.question}")

    print("🔥 Starting RAG PIPELINE...")

    # ✅ RAG pipeline
    answer, metadata_list = rag_pipeline.query(req.question, req.history)

    print("🔥 Pipeline returned ANSWER successfully")
    print(f"🔥 Answer snippet: {str(answer)[:120]}...")

    print("🔥 Building metadata objects...")

    # ✅ CRITICAL FIX: sheet_name + str()
    sources = [
        SourceMeta(
            return_name=str(m.get("return", "")),
            sheet_name=str(m.get("sheet", "")),   # ✅ FIXED
            line_code=str(m.get("line_code", "")),
            line_desc=str(m.get("line_desc", ""))
        )
        for m in metadata_list
    ]

    print("🔥 Returning ChatResponse\n")

    return ChatResponse(
        answer=answer,
        sources=sources,
        raw_metadata=metadata_list
    )
