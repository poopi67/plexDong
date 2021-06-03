# plexDong 🍆
[![PyPI](https://img.shields.io/pypi/v/flask?label=flask&style=flat-square)](https://pypi.org/project/Flask/)
[![PyPI](https://img.shields.io/pypi/v/requests?label=requests&style=flat-square)](https://pypi.org/project/requests/)
[![PyPI](https://img.shields.io/pypi/v/python-dotenv?label=python-dotenv&style=flat-square)](https://pypi.org/project/python-dotenv/)
[![Docker](https://img.shields.io/docker/v/poopi67/plexdong?logo=docker&label=version&style=flat-square)](https://hub.docker.com/r/poopi67/plexdong)

Takes the current play count from [Tautulli](https://github.com/Tautulli/Tautulli) and generates an ASCII Dong 🍆 based on the amount.

*This is intended as a joke, please do not take it seriously.*

## Installation

### Docker

`sudo docker run -h localhost -p 8787:8787  -it -e api_token=<api_token> -e server_url=<server_url> poopi67/plexdong:latest`

Simply replace the environment variables with your own and run the command.

### Manual
- You must have [Tautulli](https://github.com/Tautulli/Tautulli) installed and fully configured
- Clone the repository
- Install the requirements using `pip3 install -r requirements.txt`
- Edit the `.env` file with your Tautulli host and API key (found under `Settings > Web Interface`)
- Run it using `python3 app.py`
- Open a web browser to access `http://localhost:8787`
- Go crazy

## Example
<img src="https://i.imgur.com/mQ9UL0z.png" width="50%"><img src="https://i.imgur.com/ttQ72mn.png" width="50%">
