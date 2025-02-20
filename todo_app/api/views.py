from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.serializers import NoteSerializer
from note.models import Note


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Note.objects.for_user(user=self.request.user)
