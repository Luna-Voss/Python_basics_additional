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
        out = run(['23'])
        self.assertEqual("Tak\n", out,
                         msg="Dla liczby 23, program powinien wypisać w konsoli wiadomość: 'Tak'.")

    def test_2(self):
        out = run(['2'])
        self.assertEqual("Tak\n", out,
                         msg="Dla liczby 2, program powinien wypisać w konsoli wiadomość: 'Tak'.")

    def test_3(self):
        out = run(['4'])
        self.assertEqual("Nie\n", out,
                         msg="Dla liczby 4, program powinien wypisać w konsoli wiadomość: 'Nie'.")

    def test_4(self):
        out = run(['2000'])
        self.assertEqual("Nie\n", out,
                         msg="Dla liczby 2000, program powinien wypisać w konsoli wiadomość: 'Nie'.")

    def test_5(self):
        out = run(['1'])
        self.assertEqual("Przerywam pracę\n", out,
                         msg="Dla liczby 1, program powinien wypisać w konsoli wiadomość: 'Przerywam pracę'.")

