from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.test import TestCase, Client
from django.urls import reverse

from note.models import Note


class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()

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

        self.assertTrue('accounts/login' in response.url)

    def test_access_to_page_with_login(self):
        self.client.login(username='testuser', password='1234')
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)

    def test_delete_note_as_not_owner(self):
        self.client.login(username='otheruser', password='5678')
        response = self.client.post(reverse('delete_note', args=[self.note.pk]))

        self.assertEqual(response.status_code, 403)

    def test_delete_note_as_owner(self):
        self.client.login(username='testuser', password='1234')
        response = self.client.post(reverse('delete_note', args=[self.note.pk]))
        self.assertRedirects(response, reverse('trash'))
