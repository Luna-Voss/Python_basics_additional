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
        out = run(['32'])
        self.assertEqual(89.6, round(float(out), 2),
                         msg="32 stopnie Celsjusza to 89.6 stopnie Fahrenheita.")

    def test_2(self):
        out = run(['62'])
        self.assertEqual(143.6, round(float(out), 2),
                         msg="62 stopnie Celsjusza to 143.6 stopnie Fahrenheita.")

    def test_3(self):
        out = run(['-22'])
        self.assertEqual(-7.6, round(float(out), 2),
                         msg="-22 stopnie Celsjusza to -7.6 stopni Fahrenheita.")

    def test_4(self):
        out = run(['0'])
        self.assertEqual(32.0, round(float(out), 2),
                         msg="0 stopni Celsjusza to 32 stopnie Fahrenheita.")

