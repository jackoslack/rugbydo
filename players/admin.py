from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from players.models import Match, Person, Player, PlayerHonours, PlayerMatch, Season


@admin.register(Match)
class MatchAdmin(ImportExportModelAdmin):
    list_display = (
        "date",
        "grade",
        "opponent",
        "venue",
        "match_type",
        "points_for",
        "points_against",
        "result",
    )
    list_filter = ("date", "season", "grade", "opponent", "venue", "match_type")


@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "email", "location", "birth_date", "role")
    list_filter = ("name", "role")


@admin.register(Player)
class PlayerAdmin(ImportExportModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "current",
        "junior",
        "date_of_birth",
        "age",
    )
    list_filter = ("gender", "date_of_birth", "current", "junior")


@admin.register(PlayerHonours)
class PlayerHonoursAdmin(ImportExportModelAdmin):
    list_display = (
        "player",
        "rep_level",
        "description",
        "caps",
        "year",
        "sub_level",
        "comments",
    )
    list_filter = ("rep_level", "caps", "year", "sub_level")


@admin.register(PlayerMatch)
class PlayerMatchAdmin(ImportExportModelAdmin):
    list_display = (
        "match",
        "player",
        "position",
        "player_games",
        "tries",
        "goals",
        "fgoals",
        "pgoals",
        "player_points",
        "comments",
    )
    list_filter = (
        "position",
        "match__season",
        "match__grade",
        "match__round_number",
        "comments",
    )


@admin.register(Season)
class SeasonAdmin(ImportExportModelAdmin):
    list_display = ("year", "grade")
    list_filter = ("year", "grade")
