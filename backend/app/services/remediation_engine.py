"""
Deterministic Remediation Engine
==================================
Owner: Ritik Budhathoki (Backend Lead)
       Data sourced by: Jeshik Neupane (App Lead)

The rule-based treatment recommendation system.

Design Principle:
    Unlike AI-generated recommendations (e.g., Plantix uses LLMs which can
    hallucinate unsafe chemical advice), this engine is DETERMINISTIC.
    It maps each disease class to expert-verified treatment protocols from:
    - FAO Plant Production and Protection Guidelines (2019)
    - Peer-reviewed agricultural literature

    This eliminates any risk of hallucinated or agronomically unsafe advice.

How It Works:
    1. Receives classified disease_class string (e.g., "tomato_early_blight")
    2. Queries treatment_protocols table in PostgreSQL
    3. Returns structured treatment dict
    4. No AI, no generation, no hallucination possible

TODO (Ritik):
    - Implement get_treatment() with DB query
    - Handle "healthy" disease class gracefully
    - Handle unknown disease class with HTTP 404
    - Add caching (treatments rarely change)
"""

# from sqlalchemy.orm import Session
# from app.models.database import TreatmentProtocol


class RemediationEngine:
    """
    Deterministic rule-based treatment recommendation engine.

    Queries expert-verified treatment protocols from PostgreSQL.
    All treatments seeded from FAO guidelines and peer-reviewed literature.
    """

    def __init__(self, db_session=None):
        """
        Initialize with a database session.

        Args:
            db_session: SQLAlchemy database session.

        TODO (Ritik): Accept and store db_session
        """
        # TODO (Ritik): Store db_session
        pass

    def get_treatment(self, disease_class: str) -> dict:
        """
        Retrieve expert-verified treatment for a classified disease.

        Args:
            disease_class: Disease class string (e.g., "tomato_early_blight").

        Returns:
            dict: Treatment protocol with keys:
                  chemical_control, cultural_control, preventive_measures,
                  safety_note, source, disease_name, crop, is_healthy.

        Raises:
            ValueError: If disease_class not found in treatment_protocols table.

        TODO (Ritik):
            - Query TreatmentProtocol table by disease_class
            - Return as dict
            - Handle not found with clear error
        """
        pass

    def get_all_diseases(self) -> list:
        """
        Return all supported disease classes.

        Returns:
            list: All disease_class strings from treatment_protocols table.

        TODO (Ritik): Query all rows from treatment_protocols table
        """
        pass
