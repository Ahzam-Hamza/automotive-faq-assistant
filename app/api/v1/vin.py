from fastapi import APIRouter, HTTPException, Request
from app.services.vin_decoder import VINDecoder
from app.services.recall_service import RecallService
from app.schemas.vin_schema import (
    SuccessResponse,
    VINValidateResponse,
    VINDecodeResponse,
    VINErrorResponse,
    RecallResponse,
)
from app.core.rate_limiter import RateLimiter


router = APIRouter(prefix="/api/v1/vin", tags=["VIN v1"])

vin_decoder = VINDecoder()
recall_service = RecallService()

# Allow 5 requests per 10 seconds per IP
rate_limiter = RateLimiter(max_requests=5, window_seconds=10)


@router.get(
    "/validate/{vin}",
    response_model=SuccessResponse[VINValidateResponse]
)
async def validate_vin(vin: str, request: Request):
    """
    Validate a VIN number.
    """

    # ✅ Apply rate limiting
    client_ip = request.client.host
    if not rate_limiter.allow_request(client_ip):
        raise HTTPException(
            status_code=429,
            detail="Too many requests. Please try again later."
        )

    is_valid = vin_decoder.validate_vin(vin)

    return {
        "success": True,
        "data": {
            "vin": vin,
            "is_valid": is_valid
        }
    }


@router.get(
    "/decode/{vin}",
    response_model=SuccessResponse[VINDecodeResponse],
    responses={400: {"model": VINErrorResponse}}
)
async def decode_vin(vin: str, request: Request):
    """
    Decode VIN and return vehicle information.
    """

    # ✅ Apply rate limiting
    client_ip = request.client.host
    if not rate_limiter.allow_request(client_ip):
        raise HTTPException(
            status_code=429,
            detail="Too many requests. Please try again later."
        )

    decoded_data = vin_decoder.decode(vin)

    if "error" in decoded_data:
        raise HTTPException(
            status_code=400,
            detail=decoded_data["error"]
        )

    return {
        "success": True,
        "data": decoded_data
    }


@router.get(
    "/recalls/{vin}",
    response_model=SuccessResponse[RecallResponse]
)
async def get_recalls(vin: str, request: Request):
    """
    Get recall information for a VIN.
    """

    # ✅ Apply rate limiting
    client_ip = request.client.host
    if not rate_limiter.allow_request(client_ip):
        raise HTTPException(
            status_code=429,
            detail="Too many requests. Please try again later."
        )

    decoded_data = vin_decoder.decode(vin)

    if "error" in decoded_data:
        raise HTTPException(
            status_code=400,
            detail=decoded_data["error"]
        )

    manufacturer = decoded_data.get("manufacturer", "")
    manufacturer_name = manufacturer.split(" ")[0] if manufacturer else ""

    recalls = recall_service.check_recalls(manufacturer_name)

    return {
        "success": True,
        "data": {
            "vin": vin,
            "manufacturer": manufacturer,
            "recalls": recalls
        }
    }
