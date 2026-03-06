print("🔥 MY FASTAPI APP LOADED")

from dotenv import load_dotenv
import os, sys

load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"), override=True)

print("LOADED FILE:", __file__, flush=True)
print("CWD:", os.getcwd(), flush=True)
print("GENRUNTIME_PROVIDER:", os.getenv("GENRUNTIME_PROVIDER"), flush=True)
print("ANTHROPIC_API_KEY present?:", bool(os.getenv("ANTHROPIC_API_KEY")), flush=True)
sys.stdout.flush()
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

from genruntime import generate_structured
from genruntime.errors import ValidationError, ProviderError, GenRuntimeError

from schemas import ResumeSchema
from prompts import build_resume_extraction_prompt

app = FastAPI(title="GenRuntime Structured Extractor", version="0.1")


class ExtractRequest(BaseModel):
    document_text: str
    model: Optional[str] = None
    timeout: Optional[int] = None
    max_retries: Optional[int] = None


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/debug/env")
def debug_env():
    return {
        "GENRUNTIME_PROVIDER": os.getenv("GENRUNTIME_PROVIDER"),
        "GENRUNTIME_MODEL": os.getenv("GENRUNTIME_MODEL"),
        "ANTHROPIC_API_KEY_present": bool(os.getenv("ANTHROPIC_API_KEY")),
        "OPENAI_API_KEY_present": bool(os.getenv("OPENAI_API_KEY")),
        "cwd": os.getcwd(),
        "file": __file__,
    }

@app.post("/extract/resume")
def extract_resume(req: ExtractRequest):
    prompt = build_resume_extraction_prompt(req.document_text)

    try:
        result = generate_structured(
            prompt=prompt,
            schema=ResumeSchema,
            model=req.model,
            timeout=req.timeout,
            max_retries=req.max_retries,
        )

        # result.parsed is a ResumeSchema object (validated)
        # result.meta includes request_id/latency/tokens/etc.
        return {
            "parsed": result.parsed.model_dump(),
            "meta": result.meta.model_dump() if hasattr(result.meta, "model_dump") else dict(result.meta),
        }

    except ValidationError as e:
        raise HTTPException(status_code=422, detail=f"Validation failed: {str(e)}")
    except ProviderError as e:
        raise HTTPException(status_code=502, detail=f"Provider error: {str(e)}")
    except GenRuntimeError as e:
        raise HTTPException(status_code=500, detail=f"GenRuntime error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")