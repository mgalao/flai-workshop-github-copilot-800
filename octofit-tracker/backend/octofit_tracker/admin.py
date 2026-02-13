from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'team', 'role', 'created_at']
    search_fields = ['name', 'email', 'team']
    list_filter = ['role', 'team', 'created_at']
    ordering = ['-created_at']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'captain', 'members_count', 'created_at']
    search_fields = ['name', 'captain']
    list_filter = ['created_at']
    ordering = ['-created_at']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'activity_type', 'duration_minutes', 'calories_burned', 'date']
    search_fields = ['user_name', 'user_email', 'activity_type']
    list_filter = ['activity_type', 'date']
    ordering = ['-date']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['rank', 'user_name', 'team', 'total_activities', 'total_calories', 'total_duration_minutes']
    search_fields = ['user_name', 'user_email', 'team']
    list_filter = ['team']
    ordering = ['rank']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['name', 'activity_type', 'difficulty_level', 'estimated_duration_minutes', 'estimated_calories']
    search_fields = ['name', 'activity_type', 'difficulty_level']
    list_filter = ['activity_type', 'difficulty_level']
    ordering = ['name']
