class DummyRAG:
    def query(self, question, history=None):
        answer = f"Temporary answer for: {question}"
        metadata = [
            {
                "return": "LCR",
                "sheet": "HQLA",
                "line_code": "110",
                "line_desc": "Accrued interest on Level 1 assets"
            }
        ]
        return answer, metadata


rag_pipeline = DummyRAG()
