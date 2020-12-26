import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestNote:
    def test_init(self):
        note_obj = mixer.blend('notes.Note')
        assert note_obj.pk == 1, 'Should save an instance'

    def test_get_excerpt(self):
        note_obj = mixer.blend('notes.Note', description='This is the first note')
        result = note_obj.get_excerpt(15)
        expected = 'This is the fir'
        assert  result == expected, 'Should return first few characters'
