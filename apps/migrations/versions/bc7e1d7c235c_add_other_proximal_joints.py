"""add_other_proximal_joints

Revision ID: bc7e1d7c235c
Revises: c69efe677aec
Create Date: 2024-08-29 02:06:57.554415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc7e1d7c235c'
down_revision = 'c69efe677aec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('score_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('other_proximal_joints', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('score_data', schema=None) as batch_op:
        batch_op.drop_column('other_proximal_joints')

    # ### end Alembic commands ###
