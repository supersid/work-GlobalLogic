"""empty message

Revision ID: 9bdd70d34f87
Revises: d9f04187279c
Create Date: 2019-05-30 12:31:05.421198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bdd70d34f87'
down_revision = 'd9f04187279c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'student', 'teacher', ['id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.drop_column('student', 'id')
    # ### end Alembic commands ###