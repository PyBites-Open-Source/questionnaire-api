"""empty message

Revision ID: 2d2807ea9f86
Revises: 191c7e732d57
Create Date: 2019-10-25 21:56:24.970775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2d2807ea9f86"
down_revision = "191c7e732d57"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "category",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=80), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "question",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("question", sa.String(length=120), nullable=False),
        sa.Column("category_id", sa.Integer(), nullable=False),
        sa.Column("level", sa.String(length=30), nullable=False),
        sa.Column("true_false_question", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(["category_id"], ["category.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "answer",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("answer", sa.String(length=80), nullable=False),
        sa.Column("question_id", sa.Integer(), nullable=False),
        sa.Column("correct_answer", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(["question_id"], ["question.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("answer")
    op.drop_table("question")
    op.drop_table("category")
    # ### end Alembic commands ###