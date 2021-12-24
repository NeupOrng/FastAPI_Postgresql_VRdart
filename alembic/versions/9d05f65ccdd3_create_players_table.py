"""create players table

Revision ID: 9d05f65ccdd3
Revises:
Create Date: 2021-12-24 15:26:27.844795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d05f65ccdd3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'players',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('username', sa.String(100), nullable=False),
        sa.Column('oculus_id', sa.String(100), nullable=False, unique=True),
        sa.Column('highscore', sa.String(10), default="0"),
        sa.Column('fastest_time', sa.String(30), default="0"),
        sa.Column('coin', sa.Integer, default=0),
    )
    op.create_table(
        'darts',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('dart_name', sa.String(100), nullable=False),
        sa.Column('price', sa.Integer, nullable=False),
        sa.Column('is_owned', sa.Boolean, default=False),
        sa.Column('player_id', sa.Integer, sa.ForeignKey("players.id"), nullable=True),
    )



def downgrade():
    op.drop_table('players')
    op.drop_table('darts')
