"""Add created_at column to url table

Revision ID: b8d3b86ff1f4
Revises: 4d9a3587ca83
Create Date: 2023-06-29 19:32:01.111294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8d3b86ff1f4'
down_revision = '4d9a3587ca83'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('url', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('url', schema=None) as batch_op:
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
