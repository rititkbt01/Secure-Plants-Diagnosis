"""
Treatment / Remediation Endpoint
==================================
Owner: Ritik Budhathoki

GET /api/v1/treatment/{disease_class} — Lookup treatment for a disease.

This endpoint allows querying treatment information directly without
running inference. Useful for testing the rule engine.

TODO (Ritik):
    - Implement get_treatment endpoint
    - Validate disease_class path parameter
    - Return treatment from PostgreSQL via RemediationEngine
"""

from fastapi import APIRouter, Path, status
# from app.services.remediation_engine import RemediationEngine
# from app.models.schemas import TreatmentResponse
# from app.api.dependencies import get_current_user

router = APIRouter()


@router.get(
    "/treatment/{disease_class}",
    status_code=status.HTTP_200_OK,
    tags=["Treatment"],
    summary="Get expert-verified treatment for a disease class",
)
async def get_treatment(
    disease_class: str = Path(
        ...,
        description="Disease class identifier, e.g. 'tomato_early_blight'",
        example="tomato_early_blight",
    ),
    # current_user = Depends(get_current_user),
):
    """
    Get expert-verified treatment protocol for a specific disease class.

    Uses the deterministic rule engine — no AI generation, no hallucination risk.
    All treatments sourced from FAO guidelines and peer-reviewed literature.

    Args:
        disease_class: Disease identifier string (snake_case).

    Returns:
        TreatmentResponse: disease_name, crop, chemical_control,
                           cultural_control, preventive_measures, safety_note, source.

    Raises:
        HTTPException 404: Disease class not found in treatment database.

    TODO (Ritik):
        - Validate disease_class is a known class
        - Query treatment_protocols table via RemediationEngine
        - Return structured TreatmentResponse
    """
    pass
