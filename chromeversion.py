import os


def _extract_version(output):
    try:
        chrome_version = ''
        for letter in output[output.rindex('DisplayVersion    REG_SZ') + 24:]:
            if letter != '\n':
                chrome_version += letter
            else:
                break
        return chrome_version.strip()
    except TypeError:
        return


def get_chrome_version():
    stream = os.popen(
        'reg query "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Google Chrome"')
    output = stream.read()
    chrome_version = _extract_version(output)
    print(chrome_version)
    return chrome_version
