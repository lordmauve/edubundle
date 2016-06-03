import sys
import os
import re


def fix_script(path):
    """Fix a distlib stub .exe to use the default Python from %PATH%.
    
    The distlib stubs use a hard-coded absolute path in order to ensure
    that the scripts run with the correct Python installation rather than
    some other Python.

    However, we provide a "Command Prompt" shortcut that will ensure
    PATH is set correctly (so "python.exe" will be the correct Python).
    Therefore we can strip the absolute path and the scripts will be
    usable from the commandline in a way that can be relocated on the
    filesystem.

    """
    with open(path, 'rb') as f:
        data = f.read()

    mo = re.search(rb'#!([^\n]*)(pythonw?.exe)([\r\n]+)', data)

    if not mo:
        # This may not be one of the distlib scripts
        return
    if mo.group(1) == b'':
        # Already fixed
        return

    launcher = data[:mo.start(0)]
    zipdata = data[mo.end(0):]
    shebang = b'#!%s%s' % (mo.group(2), mo.group(3))

    with open(path, 'wb') as f:
        f.write(launcher)
        f.write(shebang)
        f.write(zipdata)


def fix_all_scripts(path):
    for f in os.listdir(path):
        p = os.path.join(path, f)
        if f.endswith(('.exe', '-script.py', '-script.pyw')):
            fix_script(p)

if __name__ == '__main__':
    fix_all_scripts(os.path.dirname(__file__))
