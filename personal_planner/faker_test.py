# Import necessary libraries and models
import random
from faker import Faker
from django.utils import timezone
from meetings.models import Meeting, Room  # replace 'your_app' with your actual app name

# Initialize Faker
fake = Faker()

# Function to generate a random meeting
def create_random_meeting():
    # Get all room ids
    room_ids = Room.objects.values_list('id', flat=True)

    # Pick a random room id
    random_room_id = random.choice(room_ids)

    meeting = Meeting(
        title=fake.sentence(nb_words=5),
        description=fake.text(),
        date=fake.date_time_this_year(before_now=False, after_now=True, tzinfo=timezone.get_current_timezone()),
        room_id=random_room_id,
        # Add other fields as necessary
    )
    return meeting

# Create and save 90 random meetings
for _ in range(90):
    meeting = create_random_meeting()
    meeting.save()