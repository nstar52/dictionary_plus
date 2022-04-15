"""empty message

Revision ID: 725a912b3833
Revises: 
Create Date: 2022-04-15 22:41:06.404942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '725a912b3833'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('word',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('translation', sa.String(length=140), nullable=True),
    sa.Column('test', sa.String(length=140), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_word_name'), 'word', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_word_name'), table_name='word')
    op.drop_table('word')
    # ### end Alembic commands ###