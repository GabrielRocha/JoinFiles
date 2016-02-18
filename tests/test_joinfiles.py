from join_files import join
import unittest
import os

BASE_DIR = os.path.dirname(__file__)


class TestJoinFiles(unittest.TestCase):
    def setUp(self):
        self.new_file = "{}/new.csv".format(BASE_DIR)

    def tearDown(self):
        os.remove(self.new_file)

    def test_create_new_file(self):
        join('{}/files'.format(BASE_DIR), self.new_file)
        self.assertTrue(os.path.exists(self.new_file))

    def test_content_new_file(self):
        join('{}/files'.format(BASE_DIR), self.new_file)
        with open(self.new_file) as file:
            content = file.readlines()
            self.assertIn('1;1;1;1;1\n', content)
            self.assertIn('2;2;2;2;2\n', content)

    def test_exec_terminal_script(self):
        os.system("python join_files.py -p tests/files -f tests/new.csv")
        with open(self.new_file) as file:
            content = file.readlines()
            self.assertIn('1;1;1;1;1\n', content)
            self.assertIn('2;2;2;2;2\n', content)

if __name__ == "__main__":
    unittest.main()