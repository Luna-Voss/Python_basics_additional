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
        out = run(['185', '70.0'])
        self.assertEqual('Zapnij pasy!\n', out,
                         msg="Osoba o wzroście 185cm oraz wadze 70kg może jechać.")

    def test_2(self):
        out = run(['150', '70.1'])
        self.assertEqual('Zapnij pasy!\n', out,
                         msg="Osoba o wzroście 150cm oraz wadze 70,1kg może jechać.")

    def test_3(self):
        out = run(['185', '180'])
        self.assertEqual('Zapnij pasy!\n', out,
                         msg="Osoba o wzroście 185cm oraz wadze 180kg może jechać.")

    def test_4(self):
        out = run(['185', '181'])
        self.assertEqual('Przykro mi, nie możesz jechać!\n', out,
                         msg="Osoba o wzroście 185cm oraz wadze 181kg nie może jechać.")

    def test_5(self):
        out = run(['149', '70.1'])
        self.assertEqual('Przykro mi, nie możesz jechać!\n', out,
                         msg="Osoba o wzroście 149cm oraz wadze 70,1kg nie może jechać.")