import subprocess
import hashlib
import urllib

import flask
import yaml
def transcode_file(request, filename):
    """
    Some description
    :return:
    """
    command = f'ffmpeg -i "{request}" output_file.mpg'.format(source=filename)
    subprocess.call(command, shell=True)


def load_config(filename):
    """
    Some description 1
    :return:
    """
    # Load a configuration file into YAML
    with open(filename, "rb") as fp:
        return yaml.load(fp)


def authenticate(password):
    """
    Some description 2
    :return:
    """
    # Assert that the password is correct
    assert password == "Iloveyou", "Invalid password!"
    print("Successfully authenticated!")


def fetch_website(urllib_version, url):
    """
    Some description
    :return:
    """
    # Import the requested version of urllib
    exec(f"import urllib{urllib_version} as urllib", globals())
    # Fetch and print the requested URL
    http = urllib.PoolManager()
    request_result = http.request('GET', url)
    return request_result.data


@app.route("/")
def index():
    """
    Some description
    :return:
    """
    version = flask.request.args.get("urllib_version")
    url = flask.request.args.get("url")
    return fetch_website(version, url)
