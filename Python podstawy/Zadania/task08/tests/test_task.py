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
        out = run(['3', '2', '5', '1', '0'])
        self.assertEqual(11, int(out),
                         msg="Dla ciągu liczb: 3, 2, 5, 1, 0, program powinien wypisać w konsoli liczbę: 11.")

    def test_2(self):
        out = run(['33', '21', '54', '-74', '0'])
        self.assertEqual(34, int(out),
                         msg="Dla ciągu liczb: 33, 21, 54, -74, 0, program powinien wypisać w konsoli liczbę: 34.")

    def test_3(self):
        out = run(['-33', '-1', '54', '-94', '0'])
        self.assertEqual(-74, int(out),
                         msg="Dla ciągu liczb: -33, -1, 54, -94, 0, program powinien wypisać w konsoli liczbę: -74.")

