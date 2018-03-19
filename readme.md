# gist-getter #

This repo holds a small script `get_gist.py` that retrieves the latest revision
of GitHub Gists given a filename.

The GitHub username is hardcoded as `joesingo` in the code. It only works for
publicly accessible gists, and if a gist contains more than one file only the
first is returned.

## Usage ##

```
pip3 install -r requirements.txt
python3 get_gist.py <filename>
```

There is also a Flask app that wraps this script and a Dockerfile to run it in
a container:

```
docker build -t gist .
docker run -p 5000:5000 gist
```

I have set this image up gist.joesingo.co.uk as a shortcut for grabbing files
quickly; e.g. `curl gist.joesingo.co.uk/tmux.conf > ~/.tmux.conf` is slightly
quicker than opening a web browser to find the URL for the gist and pasting it
somewhere...
