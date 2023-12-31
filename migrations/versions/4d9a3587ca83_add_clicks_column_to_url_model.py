"""Add clicks column to Url model

Revision ID: 4d9a3587ca83
Revises: 77be82e1b8e0
Create Date: 2023-06-29 19:01:58.070145

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d9a3587ca83'
down_revision = '77be82e1b8e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('url', schema=None) as batch_op:
        batch_op.add_column(sa.Column('clicks', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('referrers', sa.JSON(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('url', schema=None) as batch_op:
        batch_op.drop_column('referrers')
        batch_op.drop_column('clicks')

    # ### end Alembic commands ###
