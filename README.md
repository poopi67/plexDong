# plexDong 🍆
[![GitHub Release](https://img.shields.io/github/v/release/poopi67/plexDong?logo=github&include_prereleases&label=release&style=flat-square&color=F7F7F7)](https://github.com/poopi67/plexDong/releases)
[![Docker](https://img.shields.io/docker/v/poopi67/plexdong?logo=docker&label=version&style=flat-square)](https://hub.docker.com/r/poopi67/plexdong)
[![Docker](https://img.shields.io/docker/cloud/build/poopi67/plexdong?logo=docker&style=flat-square)](https://hub.docker.com/r/poopi67/plexdong/builds)
[![PyPI](https://img.shields.io/pypi/v/flask?logo=python&label=flask&style=flat-square&color=FFD43B)](https://pypi.org/project/Flask/)
[![PyPI](https://img.shields.io/pypi/v/gunicorn?logo=python&label=gunicorn&style=flat-square&color=FFD43B)](https://pypi.org/project/gunicorn/)


Takes the current play count from [Tautulli](https://github.com/Tautulli/Tautulli) and generates an ASCII Dong 🍆 based on the amount.

*This is intended as a joke, please do not take it seriously.*

## Installation

### Docker

`sudo docker run -h localhost -p 8787:8787  -it -e api_token=<api_token> -e server_url=<server_url> ghcr.io/poopi67/plexdong:latest`

Simply replace the environment variables with your own and run the command.

### Manual
- You must have [Tautulli](https://github.com/Tautulli/Tautulli) installed and fully configured
- Clone the repository
- Install the requirements using `pip3 install -r requirements.txt`
- Edit the `.env` file with your Tautulli host and API key (found under `Settings > Web Interface`)
- Run it using `gunicorn --bind 0.0.0.0:8787 wsgi:app`
- Open a web browser to access `http://localhost:8787`
- Go crazy

## Example
<img src="https://i.imgur.com/y3tK96z.png" style="width: 50%;"><img src="https://i.imgur.com/ycwl0iG.png" style="width: 50%;">
