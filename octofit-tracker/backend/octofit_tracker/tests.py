from django.test import TestCase
from django.utils import timezone
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name='Test User',
            email='test@example.com',
            team='Team Alpha',
            role='member'
        )

    def test_user_creation(self):
        """Test that a user can be created"""
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.team, 'Team Alpha')
        self.assertEqual(self.user.role, 'member')

    def test_user_str(self):
        """Test the string representation of a user"""
        self.assertEqual(str(self.user), 'Test User')


class TeamModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(
            name='Team Alpha',
            description='Test team description',
            captain='John Doe',
            members_count=5
        )

    def test_team_creation(self):
        """Test that a team can be created"""
        self.assertEqual(self.team.name, 'Team Alpha')
        self.assertEqual(self.team.description, 'Test team description')
        self.assertEqual(self.team.captain, 'John Doe')
        self.assertEqual(self.team.members_count, 5)

    def test_team_str(self):
        """Test the string representation of a team"""
        self.assertEqual(str(self.team), 'Team Alpha')


class ActivityModelTest(TestCase):
    def setUp(self):
        self.activity = Activity.objects.create(
            user_email='test@example.com',
            user_name='Test User',
            activity_type='Running',
            duration_minutes=30,
            calories_burned=300,
            distance_km=5.0,
            date=timezone.now(),
            notes='Morning run'
        )

    def test_activity_creation(self):
        """Test that an activity can be created"""
        self.assertEqual(self.activity.user_email, 'test@example.com')
        self.assertEqual(self.activity.user_name, 'Test User')
        self.assertEqual(self.activity.activity_type, 'Running')
        self.assertEqual(self.activity.duration_minutes, 30)
        self.assertEqual(self.activity.calories_burned, 300)
        self.assertEqual(self.activity.distance_km, 5.0)

    def test_activity_str(self):
        """Test the string representation of an activity"""
        self.assertEqual(str(self.activity), 'Test User - Running')


class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.entry = Leaderboard.objects.create(
            user_email='test@example.com',
            user_name='Test User',
            team='Team Alpha',
            total_activities=10,
            total_calories=1500,
            total_duration_minutes=300,
            rank=1
        )

    def test_leaderboard_creation(self):
        """Test that a leaderboard entry can be created"""
        self.assertEqual(self.entry.user_email, 'test@example.com')
        self.assertEqual(self.entry.user_name, 'Test User')
        self.assertEqual(self.entry.team, 'Team Alpha')
        self.assertEqual(self.entry.total_activities, 10)
        self.assertEqual(self.entry.total_calories, 1500)
        self.assertEqual(self.entry.rank, 1)

    def test_leaderboard_str(self):
        """Test the string representation of a leaderboard entry"""
        self.assertEqual(str(self.entry), 'Test User - Rank 1')


class WorkoutModelTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(
            name='Morning Cardio',
            description='A great morning cardio workout',
            activity_type='Cardio',
            difficulty_level='Intermediate',
            estimated_duration_minutes=45,
            estimated_calories=400,
            instructions='Warm up for 5 minutes, then...',
            recommended_for='Weight loss'
        )

    def test_workout_creation(self):
        """Test that a workout can be created"""
        self.assertEqual(self.workout.name, 'Morning Cardio')
        self.assertEqual(self.workout.activity_type, 'Cardio')
        self.assertEqual(self.workout.difficulty_level, 'Intermediate')
        self.assertEqual(self.workout.estimated_duration_minutes, 45)
        self.assertEqual(self.workout.estimated_calories, 400)

    def test_workout_str(self):
        """Test the string representation of a workout"""
        self.assertEqual(str(self.workout), 'Morning Cardio')
