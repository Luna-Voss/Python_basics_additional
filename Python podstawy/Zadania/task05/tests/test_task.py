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
        out = run(['15'])
        self.assertEqual("1\n3\n5\n7\n9\n11\n13\n15\n", out,
                         msg="Dla liczby 15, program powinien wypisać w konsoli liczby 1, 3, 5, 7, 9, 11, 13, 15.")

    def test_2(self):
        out = run(['1'])
        self.assertEqual("1\n", out,
                         msg="Dla liczby 1, program powinien wypisać w konsoli liczbę 1.")

    def test_3(self):
        out = run(['0'])
        self.assertEqual("", out,
                         msg="Dla liczby 0, program nie powinien nic wypisać w konsoli.")

