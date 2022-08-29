"""004_add_creator_id_inv_status

Revision ID: 004_add_creator_id_inv_status
Revises: 003_change_event_description
Create Date: 2022-07-30 18:39:09.662433

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from core.models.user_event import EventStatus



# revision identifiers, used by Alembic.
revision = '004_add_creator_id_inv_status'
down_revision = '003_change_event_description'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('event', sa.Column('creator_id', sa.Integer(), nullable=False))
    event_status = postgresql.ENUM(EventStatus, name="invitation_status")
    event_status.create(op.get_bind(), checkfirst=True)
    op.add_column('user_event', sa.Column('invitation_status', event_status, nullable=False))


def downgrade() -> None:
    event_status = postgresql.ENUM(EventStatus, name="invitation_status")
    event_status.drop(op.get_bind())
    op.drop_column('event', 'creator_id')
