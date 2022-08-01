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
        out = run(['ala ma kota', '1'])
        expected = "bmb nb lpub\n"
        self.assertEqual(expected, out,
                         msg="Dla tekstu Ala ma kota oraz n = 1, program powinien wypisać w konsoli: \n{}".format(expected))

    def test_2(self):
        out = run(['ala ma kota', '26'])
        expected = "ala ma kota\n"
        self.assertEqual(expected, out,
                         msg="Dla tekstu Ala ma kota oraz n = 26, program powinien wypisać w konsoli: \n{}".format(expected))

    def test_3(self):
        out = run(['to jest zdanie', '13'])
        expected = "gb wrfg mqnavr\n"
        self.assertEqual(expected, out,
                         msg="Dla tekstu To jest zdanie oraz n = 13, program powinien wypisać w konsoli: \n{}".format(expected))
