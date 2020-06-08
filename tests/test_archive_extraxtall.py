import os
import shutil
import json
import pytest

from archive import Archive


def test_archive_rar():
    """
    Test extractall for rar arvhives
    """
    path = os.getcwd()
    file_path = 'tests/assets/rar.rar'
    destination_path = ('tests/assets/extracted')
    if not os.path.exists(destination_path):
         os.makedirs(destination_path)

    rarfile = Archive(file_path)
    rarfile.extractall(destination_path)

    assert len(os.listdir(destination_path)) != 0

    shutil.rmtree(destination_path)

def test_archive_zip():
    """
    Test extractall for rar arvhives
    """
    path = os.getcwd()
    file_path = 'tests/assets/zip.zip'
    destination_path = ('tests/assets/extracted')
    if not os.path.exists(destination_path):
         os.makedirs(destination_path)

    zipfile = Archive(file_path)
    zipfile.extractall(destination_path)

    assert len(os.listdir(destination_path)) != 0

    shutil.rmtree(destination_path)

def test_archive_tar():
    """
    Test extractall for rar arvhives
    """
    path = os.getcwd()
    file_path = 'tests/assets/tar.tar.xz'
    destination_path = ('tests/assets/extracted')
    if not os.path.exists(destination_path):
         os.makedirs(destination_path)

    tarfile = Archive(file_path)
    tarfile.extractall(destination_path)

    assert len(os.listdir(destination_path)) != 0

    shutil.rmtree(destination_path)

