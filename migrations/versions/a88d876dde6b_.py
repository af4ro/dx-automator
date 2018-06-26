"""empty message

Revision ID: a88d876dde6b
Revises: 438672edda08
Create Date: 2018-03-27 23:24:16.332559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a88d876dde6b'
down_revision = '438672edda08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('user', sa.Integer(), nullable=True))
    op.drop_constraint('items_users_fkey', 'items', type_='foreignkey')
    op.create_foreign_key(None, 'items', 'users', ['user'], ['id'])
    op.drop_column('items', 'users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('users', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'items', type_='foreignkey')
    op.create_foreign_key('items_users_fkey', 'items', 'users', ['users'], ['id'])
    op.drop_column('items', 'user')
    # ### end Alembic commands ###
