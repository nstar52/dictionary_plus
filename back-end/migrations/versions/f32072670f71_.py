"""empty message

Revision ID: f32072670f71
Revises: 570ead37623c
Create Date: 2022-04-15 23:07:46.615268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f32072670f71'
down_revision = '570ead37623c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('word', sa.Column('translation', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('word', 'translation')
    # ### end Alembic commands ###