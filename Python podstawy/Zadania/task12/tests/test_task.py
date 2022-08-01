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
        arr = ["6", "5", "4", "5", "10", "5", "8", "3", "10", "6", "6", "6", "4", "3", "2", "8", "1", "3", "4", "7"]
        out = run([str(len(arr))] + arr)
        expected = "1 - 1\n2 - 1\n3 - 3\n4 - 3\n5 - 3\n6 - 4\n7 - 1\n8 - 2\n9 - 0\n10 - 2\n"
        self.assertEqual(expected, out,
                         msg="Dla tablicy {}, program powinien wypisać w konsoli: \n{}".format(arr, expected))

    def test_2(self):
        arr = ["6"]
        out = run([str(len(arr))] + arr)
        expected = "1 - 0\n2 - 0\n3 - 0\n4 - 0\n5 - 0\n6 - 1\n7 - 0\n8 - 0\n9 - 0\n10 - 0\n"
        self.assertEqual(expected, out,
                         msg="Dla tablicy {}, program powinien wypisać w konsoli: \n{}".format(arr, expected))

    def test_3(self):
        arr = ["6", "9", "2", "3", "2", "9", "10"]
        out = run([str(len(arr))] + arr)
        expected = "1 - 0\n2 - 2\n3 - 1\n4 - 0\n5 - 0\n6 - 1\n7 - 0\n8 - 0\n9 - 2\n10 - 1\n"
        self.assertEqual(expected, out,
                         msg="Dla tablicy {}, program powinien wypisać w konsoli: \n{}".format(arr, expected))

