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
        out = run(['Ala lubi koty, ale nie jest przez Koty lubiana.'])
        expected = "ala - 1\nale - 1\njest - 1\nkoty - 2\nlubi - 1\nlubiana - 1\nnie - 1\nprzez - 1\n"
        self.assertEqual(expected, out,
                         msg="Dla tekstu Ala lubi koty, ale nie jest przez Koty lubiana., program powinien wypisać w konsoli: \n{}".format(expected))

    def test_2(self):
        out = run(['Ala! lubi? koty, ale. nie jest przez Koty lubiana.'])
        expected = "ala - 1\nale - 1\njest - 1\nkoty - 2\nlubi - 1\nlubiana - 1\nnie - 1\nprzez - 1\n"
        self.assertEqual(expected, out,
                         msg="Dla tekstu Ala! lubi? koty, ale. nie jest przez Koty lubiana., program powinien wypisać w konsoli: \n{}".format(expected))

    def test_3(self):
        out = run(['World. Hello, World!'])
        expected = "hello - 1\nworld - 2\n"
        self.assertEqual(expected, out,
                         msg="Dla tekstu World. Hello, World!, program powinien wypisać w konsoli: \n{}".format(expected))
