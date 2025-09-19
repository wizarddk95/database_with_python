"""add age column to users (nullable=True)

Revision ID: 05f23cb110fb
Revises: 0b51bdd871e1
Create Date: 2025-09-19 19:26:42.816959

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '05f23cb110fb'
down_revision: Union[str, Sequence[str], None] = '0b51bdd871e1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
