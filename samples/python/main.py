import json

import client_side
import server_side


def flow_demo() -> None:
    endpoint_url = "https://company.com/api/v1/sample-endpoint"
    sa_private_key_path = "./sa-private-key.json"

    with open(sa_private_key_path) as f:
        sa_email = json.loads(f.read())["client_email"]

    print(
        "====================",
        "Calling API side:",
        "====================",
        "Getting token from Google auth server...",
        sep="\n",
    )
    token = client_side.get_id_token_from_service_account(
        svc_account_file=sa_private_key_path,
        target_audience=endpoint_url,
    )
    print(
        "Token in encoded form from auth server:",
        token,
        "Sending the request to the server...",
        "====================",
        "Server side:",
        "====================",
        "Decoding the token...",
        sep="\n",
    )
    server_side.verify_id_token(token=token, sa_email=sa_email, audience=endpoint_url)


if __name__ == "__main__":
    flow_demo()
