The demo will attempt to follow through the OAuth flow by:

- getting a token on the client side from the GCP auth server 
  using a GCP service account
- verifying and decoding the token on the server side

For this you need a service account in GCP
and an associated `.json` key file downloaded as `sa-private-key.json`
in the root directory of the repo.

```shell
# set up python virtual environment
PYTHON_VERSION="3.9.1"
VENV_NAME="svc-auth-391"
pyenv virtualenv "${PYTHON_VERSION}" "${VENV_NAME}"
pyenv local "${VENV_NAME}"
poetry install
# run example
python samples/python/main.py
```
