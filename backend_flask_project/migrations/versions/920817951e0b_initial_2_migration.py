"""Initial 2 Migration

Revision ID: 920817951e0b
Revises: a37b643c045d
Create Date: 2024-09-28 19:04:56.928165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '920817951e0b'
down_revision = 'a37b643c045d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('msroom',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nodes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.Column('mac_address', sa.String(length=17), nullable=False),
    sa.ForeignKeyConstraint(['room_id'], ['msroom.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.Column('coordinate_x', sa.Float(), nullable=True),
    sa.Column('coordinate_y', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['room_id'], ['msroom.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['msstudent.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.drop_table('nodes')
    op.drop_table('msroom')
    # ### end Alembic commands ###
