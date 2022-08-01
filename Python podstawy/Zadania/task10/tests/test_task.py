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
        out = run(['21'])
        self.assertEqual("1\n3\n7\n21\n", out,
                         msg="Dla liczby 21, program powinien wypisać w konsoli liczby: 1, 3, 7, 21.")

    def test_2(self):
        out = run(['49'])

        self.assertEqual("1\n7\n49\n", out,
                         msg="Dla liczby 49, program powinien wypisać w konsoli liczby: 1, 7, 49.")

    def test_3(self):
        out = run(['1024'])

        self.assertEqual("1\n2\n4\n8\n16\n32\n64\n128\n256\n512\n1024\n", out,
                         msg="Dla liczby 1024, program powinien wypisać w konsoli liczby: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024.")

