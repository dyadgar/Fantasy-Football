"""Helloooooooooo

Revision ID: 29ded1a06c7c
Revises: 
Create Date: 2019-12-17 22:32:42.622432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29ded1a06c7c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('team',
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.Column('team_name', sa.String(length=255), nullable=True),
    sa.Column('tactic', sa.String(length=255), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('team_id'),
    sa.UniqueConstraint('team_name')
    )
    op.create_table('players_db',
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('position', sa.String(length=255), nullable=True),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['team_id'], ['team.team_id'], ),
    sa.PrimaryKeyConstraint('player_id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('number'),
    sa.UniqueConstraint('player_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('players_db')
    op.drop_table('team')
    op.drop_table('users')
    # ### end Alembic commands ###