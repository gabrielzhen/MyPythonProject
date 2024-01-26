"""s

Revision ID: b7d94cabaa8c
Revises: e886a45848d8
Create Date: 2024-01-26 13:53:00.038843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7d94cabaa8c'
down_revision = 'e886a45848d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('about_me',
               existing_type=sa.VARCHAR(length=140),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('about_me',
               existing_type=sa.VARCHAR(length=140),
               nullable=False)

    # ### end Alembic commands ###
