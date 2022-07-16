"""002_create_table_author

Revision ID: 002_create_table_author
Revises: 001_create_table_book
Create Date: 2022-07-12 11:42:21.060206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002_create_table_author'
down_revision = '001_create_table_book'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "author",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("flname", sa.String(400), nullable=False)
    )
    op.add_column("book", sa.Column("author_id", sa.Integer, sa.ForeignKey("author.id"), nullable=False))


def downgrade() -> None:
    op.drop_column("book", "author_id")
    op.drop_table("author")
