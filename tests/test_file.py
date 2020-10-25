import os
from unittest import mock

import pytest

from src.audio_merger.file import File


def test_constructor():
    expected_path = 'D:/Desktop/05 filename.csv'
    (mock.patch('os.path.isfile').start()).side_effect = \
        lambda given_path: expected_path == given_path

    assert File(expected_path)


def test_name_extracted():
    directory_path = 'D:/theMerge/'
    file_name = '02 filename.csv'
    expected_path = os.path.join(directory_path, file_name)
    (mock.patch('os.path.isfile').start()).side_effect = \
        lambda given_path: expected_path == given_path

    file = File(expected_path)
    assert file_name == file.original_name


def test_directory_extracted():
    original_directory = 'channel_name'
    expected_path = os.path.join('D:/', original_directory, '004 filename.wav')
    (mock.patch('os.path.isfile').start()).side_effect = \
        lambda given_path: expected_path == given_path

    file = File(expected_path)
    assert original_directory == file.original_directory


def test_empty_path():
    with pytest.raises(ValueError):
        assert File('')


def test_directory():
    with pytest.raises(TypeError):
        assert File('D:/Games')


def test_original_number():
    expected_path = 'D:/Desktop/05 filename.csv'
    (mock.patch('os.path.isfile').start()).side_effect = \
        lambda given_path: expected_path == given_path

    file = File(expected_path)
    assert type(file.original_number) is int
    assert 5 == file.original_number


def test_name_without_number():
    expected_path = 'D:/files_to_merge/05 filename.csv'
    (mock.patch('os.path.isfile').start()).side_effect = \
        lambda given_path: expected_path == given_path
    file = File(expected_path)
    assert 'filename.csv' == file.name_without_number


def test_comparator():
    acceptable_files = ['D:/Games/24 frigates.wav', 'D:/Games/86 man-o-war.mp3']
    (mock.patch('os.path.isfile').start()).side_effect = \
        lambda given_path: given_path in acceptable_files

    smaller_file = File(acceptable_files[0])
    bigger_file = File(acceptable_files[1])
    assert smaller_file < bigger_file


def test_comparator_bad_input():
    acceptable_files = ['D:/folder_one/24 frigates.wav', 'D:/folder_two/86 man-o-war.mp3']
    (mock.patch('os.path.isfile').start()).side_effect = \
        lambda given_path: given_path in acceptable_files

    smaller_file = File(acceptable_files[0])
    bigger_file = File(acceptable_files[1])

    with pytest.raises(AssertionError):
        assert smaller_file < bigger_file
