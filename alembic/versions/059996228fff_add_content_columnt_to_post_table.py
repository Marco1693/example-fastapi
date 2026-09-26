"""add content columnt to post table

Revision ID: 059996228fff
Revises: ff7adaeabd1c
Create Date: 2026-09-25 13:11:59.595970

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '059996228fff'
down_revision: Union[str, Sequence[str], None] = 'ff7adaeabd1c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
