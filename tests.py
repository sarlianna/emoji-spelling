import pytest
import subprocess

from memes import (
    main,
    apply_binary_mask,
)


def test_apply_mask_results():
    source = [5, 5, 5, 5]
    mask = [0, 1, 0, 1]
    expected_result = [0, 5, 0, 5]

    result = apply_binary_mask(source, mask)
    assert result == expected_result


def test_apply_mask_differing_lengths():
    """Test that the length of the mask is used and not the source."""
    source = [5, 5, 5, 5, 5, 5, 5]
    mask = [1, 0, 0, 1]
    expected_result = [5, 0, 0, 5]

    result = apply_binary_mask(source, mask)
    assert result == expected_result

    source = [5, 5]
    mask = [1, 0, 1, 0]

    result = apply_binary_mask(source, mask)


def test_calling_script_no_options():
    completed = subprocess.run(["python3", "memes.py", "test"], stdout=subprocess.PIPE)
    expected_result = []
    print(compeleted.stdout)

    assert completed.stdout == expected_result


def test_calling_script_multipart():
    completed = subprocess.run(["python3", "memes.py", "test", "--multipart"], stdout=subprocess.PIPE)
    expected_result = []
    print(compeleted.stdout)

    assert completed.stdout == expected_result


def test_calling_script_multipart_custom_emoji():
    completed = subprocess.run(["python3", "memes.py", "test", "--multipart",
        "--space", ":test_space", "-f1", ":test:", "-f2", ":test2:", "-f3", ":test3:", "-f4", ":test4:"], stdout=subprocess.PIPE)
    expected_result = []
    print(compeleted.stdout)

    assert completed.stdout == expected_result


def test_calling_script_multipart_some_custom_emoji():
    completed = subprocess.run(["python3", "memes.py", "test", "--multipart",
                                "-f1", ":test:", "-f3", ":test3:", "-f4", ":test4:"], stdout=subprocess.PIPE)
    expected_result = []
    print(compeleted.stdout)

    assert completed.stdout == expected_result


def test_calling_with_custom_mp_pattern():
    """This feature is currently ignored."""
    completed = subprocess.run(["python3", "memes.py", "test", "--multipart",
        "--space", ":test_space", "-f1", ":test:", "-f2", ":test2:", "-f3", ":test3:", "-f4", ":test4:",
        "--mp-pattern", "[[1, 2, 3, 4, 1],[1, 2, 3, 4, 1],[1, 2, 3, 4, 1],[1, 2, 3, 4, 1],[1, 2, 3, 4, 1]]"], stdout=subprocess.PIPE)
