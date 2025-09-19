"""set default age and alter to not null

Revision ID: 1481cbe4f16a
Revises: 05f23cb110fb
Create Date: 2025-09-19 21:11:01.854126

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1481cbe4f16a'
down_revision: Union[str, Sequence[str], None] = '05f23cb110fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 기존 데이터 업데이트 (예: 전부 0으로 세팅)
    op.execute("UPDATE users SET age = 0 WHERE age IS NULL")
    
    # nullable=False로 변경
    op.alter_column('users', 'age', existing_type=sa.Integer(), nullable=False)


def downgrade() -> None:
    # 다시 nullable=True로 변경
    op.alter_column('users', 'age', existing_type=sa.Integer(), nullable=True)
