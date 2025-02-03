import os
import shlex
from shutil import which

HERE = os.path.dirname(os.path.abspath(__file__))
LABUSER_HOME = "/home/labuser"

def setup_websockify():
    vncserver = which('vncserver')
    if not vncserver:
        raise RuntimeError(
            "vncserver executable not found, please install a VNC server"
        )

    with open(vncserver) as vncserver_file:
        is_tigervnc = "tigervnc" in vncserver_file.read().casefold()

    if is_tigervnc:
        unix_socket = True
        vnc_args = [vncserver, '-rfbunixpath', "{unix_socket}"]
    else:
        unix_socket = False
        vnc_args = [vncserver, '-localhost', '-rfbport', '{port}']


    vnc_command = shlex.join(
        vnc_args
        + [
            '-verbose',
            '-fg',
            '-geometry',
            '1680x1050',
            '-SecurityTypes',
            'None',
        ]
    )

    # Construct command that runs as labuser
    command = f'cd {os.getcwd()} && HOME={LABUSER_HOME} su -s /bin/sh labuser -c "{vnc_command}"'

    print(command)
    
    return {
        'command': ['/bin/sh', '-c', command],
        'timeout': 30,
        'new_browser_window': True,
        'launcher_entry': {"title": "Desktop", "path_info": "desktop"},
        "unix_socket": unix_socket,
        "raw_socket_proxy": True,
    }
