"""initial_migration

Revision ID: 04b2bc9b7eae
Revises: 
Create Date: 2024-04-12 13:41:42.237712

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '04b2bc9b7eae'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('k_to_usd', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data')
    # ### end Alembic commands ###
