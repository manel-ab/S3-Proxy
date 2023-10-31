# S3-Proxy

-Using python3.12

-Set your own credentials of AWS (example in .env.example)

```bash
touch .env
```

# Requirements

```bash
sudo apt install python3.12
sudo apt install python3.12-venv
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Dev requirements

```bash
npm install -g pyright
pip install -r dev_requirements.txt
```

# Execution

```bash
python3.12 -m service.app
```

```bash
curl -X POST -F "file=@/Volumes/Manel/S3-Proxy/bandit.yml" http://127.0.0.1:8000/upload_file\?storage_name\=storage\&file_name\=bandit_example
```

or access to http://127.0.0.1:8000/docs
