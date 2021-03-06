"""posts table

Revision ID: 4374cf5aacbe
Revises: b9422c7adee9
Create Date: 2020-07-18 23:32:12.505572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4374cf5aacbe'
down_revision = 'b9422c7adee9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('img_filename', sa.String(), nullable=True),
    sa.Column('img_data', sa.LargeBinary(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('agent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['agent_id'], ['agent.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###
