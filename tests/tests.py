import unittest
from note_manager.data.save_notes_to_file import save_notes_to_file
from note_manager.data.load_notes_from_file import load_notes_from_file

class TestNoteManager(unittest.TestCase):
    def test_save_and_load_notes(self):
        notes = [
            {
                'username': 'Test',
                'title': 'Test Note',
                'content': 'Test Content',
                'status': 'Test Status',
                'created_date': 'Test Date',
                'issue_date': 'Test Date End'
            }
        ]
        save_notes_to_file(notes, 'test.txt')
        load_notes = load_notes_from_file('test.txt')
        self.assertEqual(notes, load_notes)


if __name__ == '__main__':
    unittest.main()