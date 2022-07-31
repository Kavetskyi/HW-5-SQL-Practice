"""003_change_event_description

Revision ID: 003_change_event_description
Revises: 002_add_event_relation
Create Date: 2022-07-30 10:48:13.497775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '003_change_event_description'
down_revision = '002_add_event_relation'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('event', 'description', existing_type=sa.VARCHAR(), nullable=True)


def downgrade() -> None:
    op.alter_column('event', 'description', existing_type=sa.VARCHAR(), nullable=False)
