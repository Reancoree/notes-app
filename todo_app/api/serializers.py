from rest_framework import serializers

from note.models import Note, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class NoteSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Note
        fields = ['id', 'title', 'text', 'color', 'time_create', 'is_deleted', 'category']
