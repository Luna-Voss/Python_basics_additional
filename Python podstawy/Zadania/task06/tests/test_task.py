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
        out = run(['4', '11'])
        self.assertEqual(60, round(float(out), 2),
                         msg="Dla liczb a = 4 oraz b = 11 program powinien wypisać w konsoli liczbę 60.")

    def test_2(self):
        out = run(['9', '64'])
        self.assertEqual(2044, round(float(out), 2),
                         msg="Dla liczb a = 9 oraz b = 64 program powinien wypisać w konsoli liczbę 2044.")

    def test_3(self):
        out = run(['2', '1'])
        self.assertEqual("Robota skończona\n", out,
                         msg="Dla liczb a = 2 oraz b = 1 program powinien wypisać w konsoli wiadomość 'Robota skończona'.")

    def test_4(self):
        out = run(['2', '2'])
        self.assertEqual("Robota skończona\n", out,
                         msg="Dla liczb a = 2 oraz b = 2 program powinien wypisać w konsoli wiadomość 'Robota skończona'.")

