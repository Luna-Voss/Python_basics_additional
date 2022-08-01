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
        out = run(['1', '-4', '2', '17', '0'])
        self.assertEqual("13\n6.5\n", out,
                         msg="Dla ciągu liczb: 1, -4, 2, 17, 0, program powinien wypisać w konsoli liczby: 13, 6.5.")

    def test_2(self):
        out = run(['11', '-44', '52', '327', '0'])
        self.assertEqual("283\n141.5\n", out,
                         msg="Dla ciągu liczb: 11, -44, 52, 327, 0, program powinien wypisać w konsoli liczby: 283, 141.5.")

    def test_3(self):
        out = run(['12', '24', '-24', '0'])
        self.assertEqual("0\n0.0\n", out,
                         msg="Dla ciągu liczb: 12, 24, -24, 0, program powinien wypisać w konsoli liczby: 0, 0.0")

