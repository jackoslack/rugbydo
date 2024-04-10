import datetime

from django.db import models
from django.urls import reverse


class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    birth_date = models.CharField(max_length=10, blank=True)
    location = models.CharField(max_length=100, blank=True)

    Coach = "C"
    Manager = "M"
    Physio = "P"
    Trainer = "T"
    NA = "-"

    MATCH_ROLE_CHOICES = (
        (Coach, "Coach"),
        (Manager, "Manager"),
        (Physio, "Physio"),
        (Trainer, "Trainer"),
        (NA, "-"),
    )

    role = models.CharField(
        max_length=2,
        choices=MATCH_ROLE_CHOICES,
        default="-",
    )


class Player(models.Model):
    ab_number = models.CharField(max_length=20, default="-", blank=True)
    myrugby_id = models.IntegerField(null=True, unique=True, default=None)
    first_name = models.CharField(max_length=100, blank=False)
    preferred_name = models.CharField(max_length=100, default="", blank=True)
    nickname = models.CharField(max_length=100, default="", blank=True)
    last_name = models.CharField(max_length=100, blank=False)
    nee_name = models.CharField(max_length=100, default="", blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    home_phone = models.CharField(max_length=12, default="", blank=True)
    mobile_phone = models.CharField(max_length=12, default="", blank=True)
    gender = models.CharField(max_length=10, default="M")
    current = models.BooleanField(default=False)
    junior = models.BooleanField(default=False)
    photo = models.ImageField(
        blank=True, upload_to="media/player_photos", default="no-image.jpg"
    )

    class Meta:
        ordering = ("last_name", "first_name", "gender")

    def get_absolute_url(self):
        return reverse("player-detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        # FIXME: deal with this at the template
        if not self.preferred_name:
            self.preferred_name = self.first_name
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    @property
    def getname(self):
        return f"{self.last_name} {self.first_name}"

    @property
    def age(self):
        if self.date_of_birth is None:
            return "NULL"
        # FIXME: use humanize or just timesince
        return int((datetime.date.today() - self.date_of_birth).days / 365)


class Match(models.Model):
    Womens = "W"
    Junior = "JR"
    Senior = "SR"
    MATCH_CATEGORY_CHOICES = (
        (Womens, "Womens"),
        (Junior, "Junior"),
        (Senior, "Senior"),
    )

    category = models.CharField(
        max_length=2,
        choices=MATCH_CATEGORY_CHOICES,
        default=Senior,
    )

    venue = models.CharField(max_length=100)
    venue_abbr = models.CharField(max_length=10)
    date = models.DateField()
    # FIXME: many of these should probably be relations
    season = models.CharField(max_length=10, blank=True)
    grade = models.CharField(max_length=20, verbose_name="Grade")
    opponent = models.CharField(max_length=20, verbose_name="Opp")
    # FIXME: should have an enumeration
    match_type = models.CharField(max_length=10, verbose_name="Type")
    round_number = models.CharField(max_length=5, default="1", verbose_name="Rnd")
    points_for = models.PositiveIntegerField(default=0, blank=False, verbose_name="For")
    points_against = models.PositiveIntegerField(
        default=0, blank=False, verbose_name="Ag"
    )
    bonus_points = models.PositiveIntegerField(
        default=0, blank=False, verbose_name="BP"
    )
    result = models.CharField(
        max_length=10, default="", blank=True, verbose_name="Result"
    )
    referee = models.CharField(
        max_length=20, default="", blank=True, verbose_name="Ref"
    )
    photo = models.ImageField(blank=True, upload_to="media/team_photos", default="")
    video_link = models.URLField(blank=True)

    class Meta:
        ordering = ["-date", "grade"]
        verbose_name = "Match"
        verbose_name_plural = "Matches"

    def get_absolute_url(self):
        return reverse("match-detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.grade}/Rnd/{self.round_number}/{self.season}"


class PlayerMatch(models.Model):
    player = models.ForeignKey("Player", on_delete=models.SET_NULL, null=True)
    match = models.ForeignKey("Match", on_delete=models.SET_NULL, null=True)
    player_number = models.PositiveIntegerField(null=True, blank=True)
    position = models.CharField(max_length=10, null=True, blank=True)
    tries = models.PositiveIntegerField(default=0, blank=False)
    goals = models.PositiveIntegerField(default=0, blank=False)
    pgoals = models.PositiveIntegerField(default=0, blank=False)
    fgoals = models.PositiveIntegerField(default=0, blank=False)
    best_fairest = models.PositiveIntegerField(default=0, blank=False)
    cards = models.CharField(max_length=20, null=True, blank=True)
    players_player = models.CharField(max_length=40, null=True, blank=True)
    player_points = models.PositiveIntegerField(default=0, blank=False)
    player_games = models.PositiveIntegerField(default=1, blank=False)
    comments = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ("match__date", "match__grade", "player_number")
        verbose_name_plural = "Player Matches"

    def get_absolute_url(self):
        return reverse("playermatch-detail", args=[str(self.id)])

    def save(self, *args, **kwargs):
        # FIXME: this should be a calculation served up by the manager
        self.player_points = (
            (self.tries * 5) + (self.goals * 2) + ((self.pgoals + self.fgoals) * 3)
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.player.first_name} {self.player.last_name}"


class PlayerYear(models.Model):
    """
    Model representing a player yearly stats.
    """

    player = models.ForeignKey("Player", on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse("playeryear-detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.player.last_name}, {self.player.first_name}"


class PlayerHonours(models.Model):
    player = models.ForeignKey("Player", on_delete=models.SET_NULL, null=True)
    rep_level = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    caps = models.PositiveIntegerField(null=True, blank=True, default=1)
    sub_level = models.CharField(max_length=12, null=True, blank=True)
    year = models.CharField(max_length=12, null=True, blank=True)
    comments = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        ordering = ("player", "rep_level", "sub_level", "description")
        verbose_name_plural = "Player Honours"

    def get_absolute_url(self):
        return reverse("playerhonours-detail", args=[str(self.id)])

    def __str__(self):
        # FIXME: performance pain when iterating
        return f"{self.player.preferred_name} {self.player.last_name}"


class Season(models.Model):
    Womens = "W"
    Junior = "JR"
    Senior = "SR"
    MATCH_CATEGORY_CHOICES = (
        (Womens, "Womens"),
        (Junior, "Junior"),
        (Senior, "Senior"),
    )

    category = models.CharField(
        max_length=2,
        choices=MATCH_CATEGORY_CHOICES,
        default=Senior,
    )

    year = models.CharField(max_length=20, verbose_name="Year")
    grade = models.CharField(max_length=20, verbose_name="Grade")
    home_ground = models.CharField(
        default="Heazlett Park", max_length=40, verbose_name="Ground"
    )
    competition = models.CharField(default="CCRU", max_length=20, verbose_name="Opp")
    coach = models.CharField(blank=True, max_length=40, verbose_name="Coach")
    manager = models.CharField(blank=True, max_length=40, verbose_name="Manager")
    points_for = models.PositiveIntegerField(default=0, blank=False, verbose_name="For")
    points_against = models.PositiveIntegerField(
        default=0, blank=False, verbose_name="Ag"
    )
    bonus_points = models.PositiveIntegerField(
        default=0, blank=False, verbose_name="BP"
    )
    table_position = models.CharField(
        blank=True, max_length=20, verbose_name="Position"
    )
    finals = models.CharField(blank=True, max_length=40, verbose_name="Finals")
    notes = models.CharField(blank=True, max_length=40, verbose_name="Notes")
    photo = models.ImageField(blank=True, upload_to="media/team_photos", default="")

    class Meta:
        ordering = ("-year", "grade")
        verbose_name = "Season"
        verbose_name_plural = "Seasons"

    def get_absolute_url(self):
        return reverse("season-detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.year} {self.grade}"

    @property
    def points_diff(self):
        # FIXME: should be a calculation
        return self.points_for - self.points_against
