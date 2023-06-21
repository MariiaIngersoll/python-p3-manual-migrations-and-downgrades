"""renamimg a column

Revision ID: 70d96d7ff7d8
Revises: 791279dd0760
Create Date: 2023-06-20 19:56:38.576891

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70d96d7ff7d8'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='color')


def downgrade() -> None:
    op.alter_column('students', 'color', new_column_name='name')
