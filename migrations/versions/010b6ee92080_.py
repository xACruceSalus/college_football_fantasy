"""empty message

Revision ID: 010b6ee92080
Revises: 978ec019e504
Create Date: 2016-08-18 18:32:12.931971

"""

# revision identifiers, used by Alembic.
revision = '010b6ee92080'
down_revision = '978ec019e504'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('player',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('team', sa.String(length=120), nullable=True),
    sa.Column('position', sa.String(length=120), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('ext_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team', sa.String(length=120), nullable=True),
    sa.Column('game_date', sa.DateTime(), nullable=True),
    sa.Column('opponent', sa.String(length=120), nullable=True),
    sa.Column('your_score', sa.Integer(), nullable=True),
    sa.Column('opponent_score', sa.Integer(), nullable=True),
    sa.Column('home', sa.Boolean(), nullable=True),
    sa.Column('week', sa.Integer(), nullable=True),
    sa.Column('season', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('player_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.Column('game', sa.Integer(), nullable=True),
    sa.Column('pass_attempts', sa.Integer(), nullable=True),
    sa.Column('pass_completions', sa.Integer(), nullable=True),
    sa.Column('pass_yards', sa.Integer(), nullable=True),
    sa.Column('pass_touchdowns', sa.Integer(), nullable=True),
    sa.Column('interceptions', sa.Integer(), nullable=True),
    sa.Column('rush_attempts', sa.Integer(), nullable=True),
    sa.Column('rush_yards', sa.Integer(), nullable=True),
    sa.Column('rush_touchdowns', sa.Integer(), nullable=True),
    sa.Column('rec_yards', sa.Integer(), nullable=True),
    sa.Column('rec_touchdowns', sa.Integer(), nullable=True),
    sa.Column('receptions', sa.Integer(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('predicted', sa.Integer(), nullable=True),
    sa.Column('extra_point_kick', sa.Integer(), nullable=True),
    sa.Column('three_point_kick', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game'], ['game.id'], ),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('PlayerData')
    op.drop_table('Game')
    op.drop_table('Player')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Player',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Player_id_seq"\'::regclass)'), nullable=False),
    sa.Column('name', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('team', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('position', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('year', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ext_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Player_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('Game',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Game_id_seq"\'::regclass)'), nullable=False),
    sa.Column('team', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('game_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('opponent', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('your_score', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('opponent_score', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('home', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('week', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('season', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Game_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('PlayerData',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"PlayerData_id_seq"\'::regclass)'), nullable=False),
    sa.Column('player_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('game', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pass_attempts', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pass_completions', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pass_yards', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pass_touchdowns', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('interceptions', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('rush_attempts', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('rush_yards', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('rush_touchdowns', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('rec_yards', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('rec_touchdowns', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('receptions', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('score', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('predicted', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('extra_point_kick', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('three_point_kick', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['game'], ['Game.id'], name='PlayerData_game_fkey'),
    sa.ForeignKeyConstraint(['player_id'], ['Player.id'], name='PlayerData_player_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='PlayerData_pkey')
    )
    op.drop_table('player_data')
    op.drop_table('game')
    op.drop_table('player')
    ### end Alembic commands ###
