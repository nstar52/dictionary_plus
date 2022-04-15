"""empty message

Revision ID: 0c8d7ec88718
Revises: 20eb50c80b7a
Create Date: 2022-04-15 23:04:09.626274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c8d7ec88718'
down_revision = '20eb50c80b7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('word') as batch_op:
        batch_op.drop_column('test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('word', sa.Column('test', sa.VARCHAR(length=140), nullable=True))
    # ### end Alembic commands ###