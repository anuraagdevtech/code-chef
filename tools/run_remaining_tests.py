#!/usr/bin/env python3
"""Run remaining-roadmap samples and deterministic regression suites."""
from pathlib import Path
import compileall
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    codes = (ROOT/'data/remaining.txt').read_text().split()
    missing = [code for code in codes if not (ROOT/'solutions'/f'{code}.py').exists()]
    if missing:
        print('Missing solutions:', ' '.join(missing), file=sys.stderr)
        return 1
    if not compileall.compile_dir(ROOT/'solutions', quiet=1):
        return 1
    commands = [('verify.py', '--remaining')]+[(script,) for script in (
        'test_remaining.py', 'test_remaining_math.py', 'test_dp_course.py',
        'test_advanced_one.py', 'test_advanced_two.py')]
    for script,*args in commands:
        print(f'Running {script}', flush=True)
        result = subprocess.run([sys.executable, str(ROOT/'tools'/script), *args], cwd=ROOT)
        if result.returncode:
            return result.returncode
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
