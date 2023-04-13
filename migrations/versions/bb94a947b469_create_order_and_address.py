"""create order and address

Revision ID: bb94a947b469
Revises: 4117dc2b5227
Create Date: 2023-04-13 09:59:31.983639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb94a947b469'
down_revision = '4117dc2b5227'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.drop_column('picture_url')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('picture_url', sa.VARCHAR(length=260), nullable=True))

    # ### end Alembic commands ###