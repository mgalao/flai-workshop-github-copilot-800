from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Clearing existing data...'))
        
        # Delete all existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Existing data cleared!'))
        self.stdout.write(self.style.WARNING('Creating teams...'))
        
        # Create teams
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Earth\'s Mightiest Heroes fighting for fitness',
            captain='Iron Man',
            members_count=0
        )
        
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League assembling for supreme fitness',
            captain='Superman',
            members_count=0
        )
        
        self.stdout.write(self.style.SUCCESS(f'Created teams: {team_marvel.name}, {team_dc.name}'))
        self.stdout.write(self.style.WARNING('Creating users...'))
        
        # Create Marvel users
        marvel_heroes = [
            {'name': 'Iron Man', 'email': 'tony.stark@marvel.com', 'role': 'captain'},
            {'name': 'Captain America', 'email': 'steve.rogers@marvel.com', 'role': 'member'},
            {'name': 'Black Widow', 'email': 'natasha.romanoff@marvel.com', 'role': 'member'},
            {'name': 'Thor', 'email': 'thor.odinson@marvel.com', 'role': 'member'},
            {'name': 'Hulk', 'email': 'bruce.banner@marvel.com', 'role': 'member'},
            {'name': 'Spider-Man', 'email': 'peter.parker@marvel.com', 'role': 'member'},
        ]
        
        # Create DC users
        dc_heroes = [
            {'name': 'Superman', 'email': 'clark.kent@dc.com', 'role': 'captain'},
            {'name': 'Batman', 'email': 'bruce.wayne@dc.com', 'role': 'member'},
            {'name': 'Wonder Woman', 'email': 'diana.prince@dc.com', 'role': 'member'},
            {'name': 'Flash', 'email': 'barry.allen@dc.com', 'role': 'member'},
            {'name': 'Aquaman', 'email': 'arthur.curry@dc.com', 'role': 'member'},
            {'name': 'Green Lantern', 'email': 'hal.jordan@dc.com', 'role': 'member'},
        ]
        
        marvel_users = []
        for hero in marvel_heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                team='Team Marvel',
                role=hero['role']
            )
            marvel_users.append(user)
        
        dc_users = []
        for hero in dc_heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                team='Team DC',
                role=hero['role']
            )
            dc_users.append(user)
        
        team_marvel.members_count = len(marvel_users)
        team_marvel.save()
        team_dc.members_count = len(dc_users)
        team_dc.save()
        
        all_users = marvel_users + dc_users
        self.stdout.write(self.style.SUCCESS(f'Created {len(all_users)} users'))
        self.stdout.write(self.style.WARNING('Creating activities...'))
        
        # Create activities
        activity_types = [
            {'type': 'Running', 'calories_range': (300, 600), 'distance': True},
            {'type': 'Cycling', 'calories_range': (250, 500), 'distance': True},
            {'type': 'Swimming', 'calories_range': (400, 700), 'distance': True},
            {'type': 'Weight Training', 'calories_range': (200, 400), 'distance': False},
            {'type': 'Yoga', 'calories_range': (150, 300), 'distance': False},
            {'type': 'Boxing', 'calories_range': (350, 650), 'distance': False},
        ]
        
        activities_created = 0
        for user in all_users:
            # Create 3-7 activities per user
            num_activities = random.randint(3, 7)
            for i in range(num_activities):
                activity_type = random.choice(activity_types)
                duration = random.randint(30, 120)
                calories = random.randint(*activity_type['calories_range'])
                days_ago = random.randint(0, 30)
                
                activity_data = {
                    'user_email': user.email,
                    'user_name': user.name,
                    'activity_type': activity_type['type'],
                    'duration_minutes': duration,
                    'calories_burned': calories,
                    'date': datetime.now() - timedelta(days=days_ago),
                    'notes': f'{user.name} completed {activity_type["type"]} workout'
                }
                
                if activity_type['distance']:
                    activity_data['distance_km'] = round(random.uniform(3, 15), 2)
                
                Activity.objects.create(**activity_data)
                activities_created += 1
        
        self.stdout.write(self.style.SUCCESS(f'Created {activities_created} activities'))
        self.stdout.write(self.style.WARNING('Creating leaderboard entries...'))
        
        # Create leaderboard entries
        for user in all_users:
            user_activities = Activity.objects.filter(user_email=user.email)
            total_activities = user_activities.count()
            total_calories = sum(a.calories_burned for a in user_activities)
            total_duration = sum(a.duration_minutes for a in user_activities)
            
            Leaderboard.objects.create(
                user_email=user.email,
                user_name=user.name,
                team=user.team,
                total_activities=total_activities,
                total_calories=total_calories,
                total_duration_minutes=total_duration,
                rank=0  # Will be calculated
            )
        
        # Calculate ranks
        leaderboard_entries = Leaderboard.objects.all().order_by('-total_calories')
        for idx, entry in enumerate(leaderboard_entries, 1):
            entry.rank = idx
            entry.save()
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(all_users)} leaderboard entries'))
        self.stdout.write(self.style.WARNING('Creating workout suggestions...'))
        
        # Create workouts
        workouts = [
            {
                'name': 'Super Soldier Circuit',
                'description': 'Captain America\'s legendary circuit training for peak human performance',
                'activity_type': 'Weight Training',
                'difficulty_level': 'Advanced',
                'estimated_duration_minutes': 60,
                'estimated_calories': 400,
                'instructions': '1. Push-ups (3 sets of 25)\n2. Pull-ups (3 sets of 15)\n3. Squats (3 sets of 30)\n4. Planks (3 sets of 2 min)\n5. Burpees (3 sets of 20)',
                'recommended_for': 'Strength building, endurance'
            },
            {
                'name': 'Web-Slinger Cardio',
                'description': 'Spider-Man\'s agility and cardio routine',
                'activity_type': 'Running',
                'difficulty_level': 'Intermediate',
                'estimated_duration_minutes': 45,
                'estimated_calories': 450,
                'instructions': '1. Warm-up jog (5 min)\n2. Sprint intervals (10 x 1 min)\n3. Jumping jacks (3 sets of 50)\n4. High knees (3 sets of 1 min)\n5. Cool-down jog (5 min)',
                'recommended_for': 'Cardio, agility, stamina'
            },
            {
                'name': 'Kryptonian Power Lift',
                'description': 'Superman\'s strength training regimen',
                'activity_type': 'Weight Training',
                'difficulty_level': 'Advanced',
                'estimated_duration_minutes': 75,
                'estimated_calories': 500,
                'instructions': '1. Deadlifts (4 sets of 10)\n2. Bench press (4 sets of 12)\n3. Squats (4 sets of 15)\n4. Overhead press (4 sets of 10)\n5. Rows (4 sets of 12)',
                'recommended_for': 'Maximum strength, muscle building'
            },
            {
                'name': 'Amazonian Warrior Flow',
                'description': 'Wonder Woman\'s balanced yoga and flexibility routine',
                'activity_type': 'Yoga',
                'difficulty_level': 'Beginner',
                'estimated_duration_minutes': 60,
                'estimated_calories': 250,
                'instructions': '1. Sun salutations (10 rounds)\n2. Warrior poses (hold each for 2 min)\n3. Tree pose (2 min each side)\n4. Cobra pose (3 sets of 1 min)\n5. Corpse pose (5 min)',
                'recommended_for': 'Flexibility, balance, mindfulness'
            },
            {
                'name': 'Speed Force Sprint',
                'description': 'Flash\'s explosive speed training workout',
                'activity_type': 'Running',
                'difficulty_level': 'Advanced',
                'estimated_duration_minutes': 40,
                'estimated_calories': 550,
                'instructions': '1. Dynamic stretching (5 min)\n2. 100m sprints (10 reps)\n3. Hill sprints (8 reps)\n4. Plyometric drills (15 min)\n5. Cool-down (5 min)',
                'recommended_for': 'Speed, explosive power, agility'
            },
            {
                'name': 'Dark Knight Combat',
                'description': 'Batman\'s martial arts and combat training',
                'activity_type': 'Boxing',
                'difficulty_level': 'Advanced',
                'estimated_duration_minutes': 60,
                'estimated_calories': 600,
                'instructions': '1. Shadow boxing (10 min)\n2. Heavy bag work (15 min)\n3. Speed bag (10 min)\n4. Defensive drills (15 min)\n5. Cool-down stretching (10 min)',
                'recommended_for': 'Combat skills, cardio, coordination'
            },
            {
                'name': 'Atlantean Swim',
                'description': 'Aquaman\'s underwater endurance workout',
                'activity_type': 'Swimming',
                'difficulty_level': 'Intermediate',
                'estimated_duration_minutes': 50,
                'estimated_calories': 500,
                'instructions': '1. Warm-up (200m easy)\n2. Freestyle intervals (10 x 100m)\n3. Backstroke (400m)\n4. Treading water (5 min)\n5. Cool-down (200m easy)',
                'recommended_for': 'Full-body workout, endurance'
            },
            {
                'name': 'Asgardian Thunder',
                'description': 'Thor\'s hammer and battle-ready training',
                'activity_type': 'Weight Training',
                'difficulty_level': 'Advanced',
                'estimated_duration_minutes': 70,
                'estimated_calories': 550,
                'instructions': '1. Sledgehammer strikes (3 sets of 20)\n2. Farmer\'s walks (4 sets of 50m)\n3. Battle ropes (3 sets of 2 min)\n4. Tire flips (3 sets of 10)\n5. Core work (15 min)',
                'recommended_for': 'Functional strength, power'
            },
        ]
        
        for workout_data in workouts:
            Workout.objects.create(**workout_data)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(workouts)} workout suggestions'))
        self.stdout.write(self.style.SUCCESS('='*50))
        self.stdout.write(self.style.SUCCESS('Database population complete!'))
        self.stdout.write(self.style.SUCCESS(f'Teams: {Team.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Users: {User.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Activities: {Activity.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Leaderboard entries: {Leaderboard.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Workouts: {Workout.objects.count()}'))
        self.stdout.write(self.style.SUCCESS('='*50))
