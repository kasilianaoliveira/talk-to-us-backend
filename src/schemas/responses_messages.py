from typing import Any, Dict, Optional

from pydantic import BaseModel


class StandardSuccessResponse(BaseModel):
    status: str = "success"
    message: str = "Operação realizada com sucesso."
    data: Optional[Any] = None


class StandardErrorResponse(BaseModel):
    status: str = "error"
    code: int
    message: str
    details: Optional[Dict[str, Any]] = None


class MessageResponse(BaseModel):
    message: str
