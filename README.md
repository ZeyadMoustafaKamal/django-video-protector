#### The video protector created by django

### How to use
- install [uv](https://docs.astral.sh/uv/getting-started/installation/)
- clone the repo
- run `uv sync`
- run `uv run manage.py migrate`
- run `uv run manage.py add_video`
- run `uv run manage.py runserver`

now open the browser in [http://127.0.0.1:8000/1](127.0.0.1:8000/1) to see the video and you can't use the url in the video tag to download the video.

### How to use the dashboard
- run `uv run manage.py createsuperuser` and enter the required fields
- go to [http://127.0.0.1:8000/admin](127.0.0.1:8000/admin) and login with your credentials

