"""empty message

Revision ID: 6785f3554a03
Revises: 8b85c1ceb8c6
Create Date: 2019-05-29 11:16:45.514243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6785f3554a03'
down_revision = '8b85c1ceb8c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('authenticated', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('student', 'authenticated')
    # ### end Alembic commands ###
