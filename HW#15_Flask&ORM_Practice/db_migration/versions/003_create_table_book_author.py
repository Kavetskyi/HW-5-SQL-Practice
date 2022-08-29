"""003_create_table_book_author

Revision ID: 003_create_table_book_author
Revises: 002_create_table_author
Create Date: 2022-07-14 17:01:43.975608

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '003_create_table_book_author'
down_revision = '002_create_table_author'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "book_author",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("book_id", sa.Integer, sa.ForeignKey("book.id"), nullable=False),
        sa.Column("author_id", sa.Integer, sa.ForeignKey("author.id"), nullable=False)
    )


def downgrade() -> None:
    op.drop_table("book_author")
