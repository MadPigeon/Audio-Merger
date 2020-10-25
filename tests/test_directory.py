import os
from unittest import mock

import pytest

from src.audio_merger.directory import Directory


def test_empty_path():
    with pytest.raises(ValueError):
        assert Directory('')


def test_file_path_denied():
    with pytest.raises(TypeError):
        assert Directory('D:/MadPigeon/05 filename.csv')


def test_not_existing_folder():
    expected_path = "D:/folder that doesn't exist"
    (mock.patch('os.path.isdir').start()).side_effect = \
        lambda given_path: not expected_path == given_path
    with pytest.raises(TypeError):
        assert Directory(expected_path)


def test_extracts_folder_name():
    directory_name = 'sample_directory'
    expected_path = os.path.join('D:/imaginary_folder', directory_name)
    (mock.patch('os.path.isdir').start()).side_effect = \
        lambda given_path: expected_path == given_path

    folder = Directory(expected_path)
    assert directory_name == folder.name


def test_folder_name_is_specific():
    directory_name = 'sample_directory'
    expected_path = os.path.join('D:/imaginary_folder', directory_name)
    (mock.patch('os.path.isdir').start()).side_effect = \
        lambda given_path: expected_path == given_path
    wrong_name = 'different directory'

    folder = Directory(expected_path)
    assert wrong_name != folder.name
