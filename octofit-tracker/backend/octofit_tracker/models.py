from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default='member')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    captain = models.CharField(max_length=200)
    members_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'teams'
    
    def __str__(self):
        return self.name


class Activity(models.Model):
    user_email = models.EmailField()
    user_name = models.CharField(max_length=200)
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    calories_burned = models.IntegerField()
    distance_km = models.FloatField(null=True, blank=True)
    date = models.DateTimeField()
    notes = models.TextField(blank=True)
    
    class Meta:
        db_table = 'activities'
        verbose_name_plural = 'Activities'
    
    def __str__(self):
        return f"{self.user_name} - {self.activity_type}"


class Leaderboard(models.Model):
    user_email = models.EmailField()
    user_name = models.CharField(max_length=200)
    team = models.CharField(max_length=100)
    total_activities = models.IntegerField(default=0)
    total_calories = models.IntegerField(default=0)
    total_duration_minutes = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'leaderboard'
        ordering = ['-total_calories']
    
    def __str__(self):
        return f"{self.user_name} - Rank {self.rank}"


class Workout(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    activity_type = models.CharField(max_length=100)
    difficulty_level = models.CharField(max_length=50)
    estimated_duration_minutes = models.IntegerField()
    estimated_calories = models.IntegerField()
    instructions = models.TextField()
    recommended_for = models.CharField(max_length=200, blank=True)
    
    class Meta:
        db_table = 'workouts'
    
    def __str__(self):
        return self.name
