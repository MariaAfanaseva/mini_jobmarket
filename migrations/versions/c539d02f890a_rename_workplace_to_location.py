"""Rename workplace to location.

Revision ID: c539d02f890a
Revises:
Create Date: 2021-03-12 09:33:21.267981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c539d02f890a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vacancies', 'workplace', nullable=False, new_column_name='location')
    op.alter_column('vacancies', 'workplace_postcode', nullable=False, new_column_name='location_postcode')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vacancies', sa.Column('workplace_postcode', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('vacancies', sa.Column('workplace', sa.VARCHAR(length=128), autoincrement=False, nullable=True))
    op.drop_column('vacancies', 'location_postcode')
    op.drop_column('vacancies', 'location')
    # ### end Alembic commands ###
