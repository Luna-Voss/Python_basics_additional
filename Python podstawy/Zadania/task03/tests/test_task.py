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
        out = run(['5400'])
        self.assertEqual(415.98, round(float(out), 2),
                         msg="Podatek od 5.400zł wynosi 415,98zł.")

    def test_2(self):
        out = run(['543200.54'])
        self.assertEqual(161294.23, round(float(out), 2),
                         msg="Podatek od 543.200,54zł wynosi 161.294,23zł.")

    def test_3(self):
        out = run(['0'])
        self.assertEqual(0.0, round(float(out), 2),
                         msg="Podatek od 0,00zł wynosi 0,00zł.")

    def test_4(self):
        out = run(['320.0'])
        self.assertEqual(0.0, round(float(out), 2),
                         msg="Podatek od 320,00zł wynosi 0,00zł.")

