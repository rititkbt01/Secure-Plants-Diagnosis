"""
Database Connection Manager
=============================
Owner: Ritik Budhathoki

Sets up SQLAlchemy engine and session factory for PostgreSQL.

TODO (Ritik):
    - Configure engine with DATABASE_URL from settings
    - Create SessionLocal factory
    - Implement create_tables() to initialise schema on startup
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from app.config import settings
# from app.models.database import Base


# TODO (Ritik): Create engine from settings.DATABASE_URL
# engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

# TODO (Ritik): Create session factory
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_tables():
    """
    Create all database tables defined in ORM models.

    Called during application startup if tables don't exist.

    TODO (Ritik):
        - Call Base.metadata.create_all(bind=engine)
    """
    pass


def seed_treatment_data():
    """
    Populate treatment_protocols table from JSON seed file.

    Reads: backend/app/database/seed_data/treatment_protocols.json
    Inserts all treatment records if table is empty.

    TODO (Ritik):
        - Read treatment_protocols.json
        - Check if table is already populated (skip if yes)
        - Insert all records using SQLAlchemy session
    """
    pass
