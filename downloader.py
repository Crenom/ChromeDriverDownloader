import os
import requests
import psutil
import lxml
from bs4 import BeautifulSoup
import zipfile


def _extract_main_version(chrome_version: str) -> str:
    main_verion = chrome_version.split('.')[0]
    return main_verion


def _get_win32_link(main_version: str) -> str:
    response = requests.get('https://chromedriver.chromium.org', timeout=180, verify=False)
    soup = BeautifulSoup(response.text, 'lxml')

    for link in soup.findAll('a'):
        if f'ChromeDriver {main_version}' in link.text:
            link_text = link.text
            version = link_text.replace('ChromeDriver ', '')
            return f'https://chromedriver.storage.googleapis.com/{version}/chromedriver_win32.zip'


def _download_zip(url: str):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True, verify=False) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename


def _kill_chromedriver():
    # PROCNAME = "python.exe"
    #
    # for proc in psutil.process_iter():
    #     # check whether the process name matches
    #     if proc.name() == PROCNAME:
    #         proc.kill()
    pass


def _extract_zip(path_to_extract=None):
    with zipfile.ZipFile('chromedriver_win32.zip', 'r') as zip_ref:
        _kill_chromedriver()
        zip_ref.extractall(path_to_extract)


def _del_zip():
    os.remove('chromedriver_win32.zip')


def download_chrome_driver(chrome_version: str, path_to_download=None):
    main_version = _extract_main_version(chrome_version)
    main_link = _get_win32_link(main_version)
    _download_zip(main_link)
    _extract_zip(path_to_download)
    _del_zip()
