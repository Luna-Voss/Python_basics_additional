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
        out = run(['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'])
        expected = "Lorem ipsum dolor sit amet-MAKARENA consectetur adipiscing elit-MAKARENA sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n"
        self.assertEqual(expected, out,
                         msg="Dla tekstu Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua., program powinien wypisać w konsoli: \n{}".format(expected))

    def test_2(self):
        out = run(['A simple, text, really, so, simple!'])
        expected = "A simple-MAKARENA text-MAKARENA really-MAKARENA so-MAKARENA simple!\n"
        self.assertEqual(expected, out,
                         msg="Dla tekstu A simple, text, really, so, simple!, program powinien wypisać w konsoli: \n{}".format(expected))
