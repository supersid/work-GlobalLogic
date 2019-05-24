"""empty message

Revision ID: 0953fcdbf205
Revises: 
Create Date: 2019-05-24 12:23:56.792579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0953fcdbf205'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teacher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subcode', sa.String(length=80), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('password', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('admno', sa.Integer(), nullable=False),
    sa.Column('section', sa.String(length=80), nullable=True),
    sa.Column('Name', sa.String(length=80), nullable=True),
    sa.Column('password', sa.String(length=80), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['teacher.id'], ),
    sa.PrimaryKeyConstraint('admno')
    )
    op.create_table('marks',
    sa.Column('no', sa.Integer(), nullable=False),
    sa.Column('admno', sa.Integer(), nullable=True),
    sa.Column('marks', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['admno'], ['student.admno'], ),
    sa.ForeignKeyConstraint(['id'], ['teacher.id'], ),
    sa.PrimaryKeyConstraint('no')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('marks')
    op.drop_table('student')
    op.drop_table('teacher')
    # ### end Alembic commands ###