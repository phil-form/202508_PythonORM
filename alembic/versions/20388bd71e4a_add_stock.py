"""add_stock

Revision ID: 20388bd71e4a
Revises: cae76c45023f
Create Date: 2025-08-21 16:47:07.313697

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20388bd71e4a'
down_revision: Union[str, Sequence[str], None] = 'cae76c45023f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
