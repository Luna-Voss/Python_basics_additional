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
        out = run(['10', '10'])
        self.assertEqual(512.50, round(float(out), 2),
                         msg="Rata od kwoty 10.00 na 10 miesięcy wynosi 512.50 pownieważ kwota została podniesiona do 5,000.00.")

    def test_2(self):
        out = run(['100000', '10'])
        self.assertEqual(512.50, round(float(out), 2),
                         msg="Rata od kwoty 10,000.00 na 10 miesięcy wynosi 512.50 ponieważ kwota została pomniejszona do 5,000.00.")

    def test_3(self):
        out = run(['1000', '50'])
        self.assertEqual(30.56, round(float(out), 2),
                         msg="Rata od kwoty 1,000.00 na 50 miesięcy wynosi 30.56 ponieważ ilość rat została zmniejszona do 36.")

    def test_4(self):
        out = run(['1000', '2'])
        self.assertEqual(30.56, round(float(out), 2),
                         msg="Rata od kwoty 1,000.00 na 2 miesięcy wynosi 30.56 ponieważ ilość rat została zwiększona do 36.")

    def test_5(self):
        out = run(['7500.50', '36'])
        self.assertEqual(229.18, round(float(out), 2),
                         msg="Rata od kwoty 7,500.50 na 36 miesięcy wynosi 229.18.")

