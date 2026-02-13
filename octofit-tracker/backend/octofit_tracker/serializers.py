from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'team', 'role', 'created_at']
        read_only_fields = ['created_at']


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'captain', 'members_count', 'created_at']
        read_only_fields = ['created_at']


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    
    class Meta:
        model = Activity
        fields = ['id', 'user_email', 'user_name', 'activity_type', 'duration_minutes', 
                  'calories_burned', 'distance_km', 'date', 'notes']


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user_email', 'user_name', 'team', 'total_activities', 
                  'total_calories', 'total_duration_minutes', 'rank', 'updated_at']
        read_only_fields = ['updated_at']


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'activity_type', 'difficulty_level', 
                  'estimated_duration_minutes', 'estimated_calories', 'instructions', 
                  'recommended_for']
