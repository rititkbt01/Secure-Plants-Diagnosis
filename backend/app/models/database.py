"""
SQLAlchemy ORM Models
======================
Owner: Ritik Budhathoki

Defines database table structures as Python classes.

Tables:
    - User            — Registered users (id, username, email, password_hash)
    - TreatmentProtocol — Disease-to-treatment mappings (rule engine data)
    - DiagnosisHistory  — Audit log of all diagnoses

Reference: docs/architecture/database-schema.md

TODO (Ritik):
    - Define User model with all columns
    - Define TreatmentProtocol model with all columns
    - Define DiagnosisHistory model with all columns
    - Add table indexes (see database-schema.md)
"""

from sqlalchemy import Column, String, Boolean, Integer, Float, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class User(Base):
    """
    Registered user accounts.

    TODO (Ritik):
        - Add all columns: id (UUID PK), username, email, password_hash, is_active, timestamps
        - Add UniqueConstraint on username and email
    """

    __tablename__ = "users"

    # TODO (Ritik): Define all columns here
    pass


class TreatmentProtocol(Base):
    """
    Expert-verified treatment protocols for each disease class.

    This table is READ ONLY at runtime (populated by seed script).
    The deterministic rule engine queries this table for every diagnosis.

    TODO (Ritik):
        - Add all columns: id, disease_class (unique), disease_name, crop,
          is_healthy, chemical_control, cultural_control, preventive_measures,
          safety_note, source, created_at
    """

    __tablename__ = "treatment_protocols"

    # TODO (Ritik): Define all columns here
    pass


class DiagnosisHistory(Base):
    """
    Audit trail of all diagnoses performed.

    Note: Images are NEVER stored. Only SHA-256 hash for audit purposes.

    TODO (Ritik):
        - Add all columns: id (UUID PK), user_id (FK), disease_class,
          disease_name, confidence, image_hash, inference_ms, created_at
    """

    __tablename__ = "diagnosis_history"

    # TODO (Ritik): Define all columns here
    pass
