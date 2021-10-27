from typing import Optional

import google.oauth2


PROJECT_ID = "company-sample-project"
SA_NAME = "sample-service"
SA_EMAIL = f"{SA_NAME}@{PROJECT_ID}.iam.gserviceaccount.com"


def verify_id_token(token: str, audience: Optional[str] = None) -> bool:
    request = google.auth.transport.requests.Request()
    try:
        id_info = google.oauth2.id_token.verify_oauth2_token(
            token,
            request,
            audience=audience
        )
    except ValueError:
        print("Unable to verify token.")

        return False

    print("Token in decoded form, verified with aud:", id_info, sep="\n")

    return id_info["email"] == SA_EMAIL
