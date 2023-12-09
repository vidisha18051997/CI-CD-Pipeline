import tempfile

import pytest

from pgbackup import storage


@pytest.fixture
def infile():
    infile = tempfile.TemporaryFile("r+b")
    infile.write(b"Testing")
    infile.seek(0)
    return infile


# Local storage tests...
def test_storing_file_on_s3(mocker, infile):
    """
    Writes content from one readable to S3
    """
    client = mocker.Mock()
    storage.s3(client, infile, "bucket", "file-name")
    client.upload_fileobj.assert_called_with(infile, "bucket", "file-name")
