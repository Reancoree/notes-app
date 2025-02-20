import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from note.models import Note


@pytest.mark.django_db
class TestNoteView:
    @pytest.fixture(autouse=True)
    def setup(self, client):
        self.client = client

        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@test.ru',
            password='1234'
        )

        self.other_user = User.objects.create_user(
            username='otheruser',
            password='5678',
        )

        self.note = Note.objects.create(
            user=self.user,
            title='Test title',
            text='Test text',
        )

    def test_access_to_page_without_login(self):
        self.client.logout()
        response = self.client.get(reverse('index'))

        assert response.status_code == 302
        assert 'accounts/login' in response.url

    def test_access_to_page_with_login(self):
        self.client.login(username='testuser', password='1234')
        response = self.client.get(reverse('index'))

        assert response.status_code == 200

    def test_delete_note_as_not_owner(self):
        self.client.login(username='otheruser', password='5678')
        response = self.client.post(reverse('delete_note', args=[self.note.pk]))

        assert response.status_code == 403

    def test_delete_note_as_owner(self):
        self.client.login(username='testuser', password='1234')
        response = self.client.post(reverse('delete_note', args=[self.note.pk]))

        assert response.status_code == 302
        assert response.url == reverse('trash')
