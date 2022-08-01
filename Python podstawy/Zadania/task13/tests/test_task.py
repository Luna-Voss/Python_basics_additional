import unittest


def run(lines):
    try:
        import traceback
    except:
        return "can't import traceback"
    try:
        import os
        import pathlib
        import subprocess
        import sys
        file_dir = pathlib.Path(__file__).absolute().parent
        cmd = [sys.executable, str(file_dir.parent / 'task.py')]
        proc = subprocess.Popen(cmd,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                stdin=subprocess.PIPE,
                                encoding='utf-8',   # also for universal newlines
                                )
        # we need to use '\n' even on Windows
        stdout, stderr = proc.communicate('\n'.join(lines) + '\n')
        # if everything is fine, stderr is empty
        return stdout + stderr
    except:
        return f"cwd: {os.getcwd()}\n{traceback.format_exc()}"


class TestCase(unittest.TestCase):
    def test_1(self):
        out = run(['Python'])
        expected = "Znalazłem Python\nZaczyna się od Python\nKończy się na Python\nRówna się Python\n0\n"
        self.assertEqual(expected, out,
                         msg="Dla tekstu Python, program powinien wypisać w konsoli: \n{}".format(expected))

    def test_2(self):
        out = run(['Kurs python od podstaw to najlepsza droga do poznania Python'])
        expected = "Znalazłem Python\nKończy się na Python\n54\n"
        self.assertEqual(expected, out,
                         msg="Dla tekstu Kurs python od podstaw to najlepsza droga do poznania Python, program powinien wypisać w konsoli: \n{}".format(expected))

    def test_3(self):
        out = run(['Tylko Python!'])
        expected = "Znalazłem Python\n6\n"
        self.assertEqual(expected, out,
                         msg="Dla tekstu Tylko Python!, program powinien wypisać w konsoli: \n{}".format(expected))
