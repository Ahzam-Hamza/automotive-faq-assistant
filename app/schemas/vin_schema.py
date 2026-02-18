from pydantic import BaseModel
from pydantic import BaseModel
from typing import Generic, TypeVar
from pydantic.generics import GenericModel

T = TypeVar("T")


class SuccessResponse(GenericModel, Generic[T]):
    success: bool = True
    data: T



class VINValidateResponse(BaseModel):
    vin: str
    is_valid: bool


class VINDecodeResponse(BaseModel):
    vin: str
    manufacturer: str
    model_year: int | str


class VINErrorResponse(BaseModel):
    detail: str

from typing import List


class RecallItem(BaseModel):
    campaign_id: str
    issue: str
    severity: str


class RecallResponse(BaseModel):
    vin: str
    manufacturer: str
    recalls: List[RecallItem]
