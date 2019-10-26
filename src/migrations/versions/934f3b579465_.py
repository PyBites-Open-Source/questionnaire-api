"""empty message

Revision ID: 934f3b579465
Revises: 798672a50ee1
Create Date: 2019-10-24 21:20:56.127457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "934f3b579465"
down_revision = "798672a50ee1"
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