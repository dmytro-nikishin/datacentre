"""services table

Revision ID: 301471e048c7
Revises: 
Create Date: 2019-10-09 01:21:37.553475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '301471e048c7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('service',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('clientname', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_service_clientname'), 'service', ['clientname'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_service_clientname'), table_name='service')
    op.drop_table('service')
    # ### end Alembic commands ###