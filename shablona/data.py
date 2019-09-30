"""shablona.data: download and read data."""
import os
import sys
import contextlib
import os.path as op
from hashlib import md5
from shutil import copyfileobj

if sys.version_info[0] < 3:
    from urllib2 import urlopen, urljoin
else:
    from urllib.request import urlopen, urljoin

# Set a user-writeable file-system location to put files:
SHABLONA_HOME = op.join(os.path.expanduser('~'), '.shablona')

def get_file_data(fname, url):
    """
    Put data from a URL into a local file.

    Paramters
    ---------
    fname : str
       Local file-name for the resulting data file.

    url : str
        The URL of the remote file to download.
    """
    with contextlib.closing(urlopen(url)) as opener:
        with open(fname, 'wb') as data:
            copyfileobj(opener, data)


def get_file_md5(filename):
    """
    Compute the md5 checksum of a file.

    Parameters
    ----------
    filename : string
       The name of the file.

    Returns
    -------
    md5 checksum of the file contents
    """
    md5_data = md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(128*md5_data.block_size), b''):
            md5_data.update(chunk)
    return md5_data.hexdigest()


def check_md5(filename, stored_md5=None):
    """
    Compute the md5 checksum of a file and validate against stored checksum.

    Parameters
    -----
    filename : string
        Path to a file.
    stored_md5 : string
        Known md5 of filename to check against. If None (default), checking is
        skipped.
    """
    if stored_md5 is not None:
        computed_md5 = _get_file_md5(filename)
        if stored_md5 != computed_md5:
            msg = """The downloaded file, %s, does not have the expected md5
   checksum of "%s". Instead, the md5 checksum was: "%s". This could mean that
   something is wrong with the file or that the upstream file has been changed.
   """ % (filename, stored_md5, computed_md5)
            raise ValueError(msg)


def fetch_data(files, folder, data_size=None):
    """
    Download files to folder and validate their md5 checksums.

    Parameters
    ----------
    files : dictionary

        For each file in `files` the key should be the local file name and the value
        should be (url, md5). The file will be downloaded from url if the file
        does not already exist or if the file exists but the md5 checksum does
        not match.

    folder : str
        The directory where to save the file, the directory will be created if
        it does not already exist.
    data_size : str, optional
        A string describing the size of the data (e.g. "91 MB") to be logged to
        the screen. Default does not produce any information about data size.

    Raises
    ------
    ValueError
        Raises if the md5 checksum of the file does not match the expected
        value. The downloaded file is not deleted when this error is raised.

    """
    if not os.path.exists(folder):
        print("Creating new folder %s" % (folder))
        os.makedirs(folder)

    if data_size is not None:
        print('Data size is approximately %s' % data_size)

    all_skip = True
    for f in files:
        url, md5 = files[f]
        fullpath = pjoin(folder, f)
        if os.path.exists(fullpath) and (get_file_md5(fullpath) == md5):
            continue
        all_skip = False
        print('Downloading "%s" to %s' % (f, folder))
        get_file_data(fullpath, url)
        check_md5(fullpath, md5)
    if all_skip:
        msg = 'Dataset is already in place. If you want to fetch it again '
        msg += 'please first remove the folder %s ' % folder
        print(msg)
    else:
        print("Files successfully downloaded to %s" % (folder))


def fetch_shablona_data(data_size="16 kb"):
    """

    """
    # This is the URL to figshare data repository:
    base_url = "https://ndownloader.figshare.com/articles/2543089/versions/2"
    files = {"ortho.csv": (urljoin(base_url, "ortho.csv"),
                           '001eff7cf46bc57220bc6288e6c21563'),
             "para.csv": (urljoin(base_url, "para.csv"),
                          'a0252d4ac6e0846f87e9d8995c79070e')}

    fetch_data(files, SHABLONA_HOME, data_size=data_size)
    return files

def read_shablona_data():
    files = fetch_shablona_data()
    for k in files.keys:
