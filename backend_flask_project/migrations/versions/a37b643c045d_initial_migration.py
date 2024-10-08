"""Initial migration

Revision ID: a37b643c045d
Revises: 
Create Date: 2024-09-28 18:58:29.767028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a37b643c045d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('msstudent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_nim', sa.String(length=15), nullable=False),
    sa.Column('is_registered', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('msstudent')
    # ### end Alembic commands ###
