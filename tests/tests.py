"""Import appropriate modules to select src filepath"""
import sys
import os

current_script_dir = os.path.dirname(__file__)

src_dir = os.path.join(current_script_dir, "..", "src")

sys.path.append(src_dir)

from source_code import add

def test_func():
    result = source_code.add(1, 2)
    expected_result = 3

    assert result == expected_result
