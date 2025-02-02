import os
from .server_extension import load_jupyter_server_extension

HERE = os.path.dirname(os.path.abspath(__file__))
PARENT = os.path.dirname(HERE)

def _jupyter_server_extension_points():
    """
    Set up the server extension for collecting metrics
    """
    return [{"module": "jupyter_remote_desktop_proxy"}]

def _jupyter_server_config_dir():
    """
    Return the location of jupyter-server configuration files
    """
    return os.path.join(PARENT, 'jupyter-config', 'jupyter_server_config.d')

def _jupyter_notebook_config_dir():
    """
    Return the location of jupyter-notebook configuration files
    """
    return os.path.join(PARENT, 'jupyter-config', 'jupyter_notebook_config.d')

# For backward compatibility
_load_jupyter_server_extension = load_jupyter_server_extension
_jupyter_server_extension_paths = _jupyter_server_extension_points
