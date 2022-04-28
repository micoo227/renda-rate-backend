from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Rating

# The serializer translates a Rating object into a format that
# can be stored in our database. We use the Rating model.
class RatingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rating
    # The id is automatically created as a primary key by our Django model
    # and we can included it here as well.
    fields = ('id', 'username', 'song', 'artist', 'rating')

