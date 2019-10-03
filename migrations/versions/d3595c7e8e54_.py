"""empty message

Revision ID: d3595c7e8e54
Revises: 
Create Date: 2019-09-20 19:32:18.336751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d3595c7e8e54"
down_revision = None
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
        sa.Column("categoryid", sa.Integer(), nullable=False),
        sa.Column("level", sa.String(length=30), nullable=False),
        sa.Column("true_false_question", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(["categoryid"], ["category.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "answer",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("answer", sa.String(length=80), nullable=False),
        sa.Column("questionid", sa.Integer(), nullable=False),
        sa.Column("correct_answer", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(["questionid"], ["question.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user_answer",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("questionid", sa.Integer(), nullable=True),
        sa.Column("answerid", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["answerid"], ["answer.id"]),
        sa.ForeignKeyConstraint(["questionid"], ["question.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user_answer")
    op.drop_table("answer")
    op.drop_table("question")
    op.drop_table("category")
    # ### end Alembic commands ###