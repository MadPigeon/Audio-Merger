import os
from unittest.mock import Mock, patch

import pytest

from src.audio_merger.directory import Directory
from src.audio_merger.file import File


def test_empty_path():
    with pytest.raises(ValueError):
        assert Directory('')


def test_file_path_denied():
    with pytest.raises(TypeError):
        assert Directory('D:/MadPigeon/05 filename.csv')


def test_not_existing_folder():
    directory_path = "D:/folder that doesn't exist"
    mock_accept_dir_path(directory_path)
    with pytest.raises(TypeError):
        assert Directory(directory_path)


def test_extracts_folder_name():
    directory_name = 'sample_directory'
    directory_path = os.path.join('D:/imaginary_folder', directory_name)
    mock_accept_dir_path(directory_path)

    folder = Directory(directory_path)
    assert directory_name == folder.name


def test_folder_name_is_specific():
    directory_name = 'sample_directory'
    directory_path = os.path.join('D:/imaginary_folder', directory_name)
    wrong_name = 'different directory'

    mock_accept_dir_path(directory_path)

    folder = Directory(directory_path)
    assert wrong_name != folder.name


def test_produces_given_files():
    directory_path = 'D:/any folder/any sub-folder'
    mock_accept_dir_path(directory_path)

    list_dir_patch = patch('os.listdir')
    list_dir_patch.side_effect = ['1 file1.txt', '2 file2.txt']
    list_dir_patch.start()

    file_patch = patch('src.audio_merger.file')
    file_patch.spec = File
    file_patch.spec_set = True
    file_patch.start()
    # (patch('os.path.listdir').start()).side_effect = \
    #     lambda given_path: directory_path == given_path

    # test = os.listdir('C:/Users/С‘/PycharmProjects/Test/venv')

    assert Directory(directory_path)


def mock_accept_dir_path(expected_paths):
    (patch('os.path.isdir').start()).side_effect = \
        lambda given_path: given_path in expected_paths
