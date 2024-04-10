import django_tables2 as tables

from players.models import Player, PlayerMatch


class PlayerTable(tables.Table):
    class Meta:
        model = Player


class PlayerMatchTable(tables.Table):
    class Meta:
        model = PlayerMatch


class StatsTable(tables.Table):
    class Meta:
        model = PlayerMatch
