import google.auth.transport.requests
import google.oauth2.service_account


def get_id_token_from_service_account(svc_account_file: str, target_audience: str):
    id_token_credentials = (
        google.oauth2.service_account.IDTokenCredentials.from_service_account_file(
            svc_account_file,
            target_audience=target_audience
        )
    )

    request = google.auth.transport.requests.Request()
    id_token_credentials.refresh(request)

    return id_token_credentials.token
