"""new fields in users table

Revision ID: 413407c16f5e
Revises: fd81006cfa1b
Create Date: 2020-07-19 14:53:48.695766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '413407c16f5e'
down_revision = 'fd81006cfa1b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('agent', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('agent', sa.Column('contact', sa.String(length=140), nullable=True))
    op.add_column('agent', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('agent', 'last_seen')
    op.drop_column('agent', 'contact')
    op.drop_column('agent', 'about_me')
    # ### end Alembic commands ###