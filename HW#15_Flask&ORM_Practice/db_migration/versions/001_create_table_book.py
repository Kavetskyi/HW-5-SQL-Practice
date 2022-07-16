"""initial

Revision ID: 001_create_table_book
Revises: 
Create Date: 2022-07-12 09:41:01.721803

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001_create_table_book'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "book",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("title", sa.String(500), nullable=False)
    )


def downgrade() -> None:
    op.drop_table("book")
