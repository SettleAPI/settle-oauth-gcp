In this scenario, the *Client Service* is your service and the *API Server*
is the Settle API server.

To access a Settle endpoint, your service needs a *service account key*
and an *audience*, which is the URL of the Settle API server endpoint.

After creating a *service account* in GCP, you can obtain
an associated *service account key* in GCP.

You must supply your *service account email* to Settle before
you can use its associated *service account key* to access the Settle API Server.
We will register it in our system and inform you when it becomes active.

When connecting to the Settle API server,
you will transmit the token as part of the request headers
in the `Authorization: Bearer <TOKEN>` form.

## Creating a GCP service account and key

To connect to Settle, you'll need a GCP service account.

After creating the service account, you'll need to create a key to use it in your API.

!!! IMPORTANT
    The key will only be provided at creation time, so make sure to save it then.

Settle provides access to two environments: *production* and *sandbox*.
You will thus need to create two service accounts, one for each environment.
While you could have both service accounts in a single GCP project:

```yaml
projects:
- global:
    users: [admins@example.com]
    service_accounts: [example-service-prod, example-service-demo]
```

we recommend you create one project with one service account for each environment:

```yaml
projects:
- production:
    users: [admins@example.com]
    service_accounts: [example-service]
- sandbox:
    users: [admins@example.com, devs@example.com]
    service_accounts: [example-service]
```

The recommended approach will allow you to provide easy sandbox access to devs
while keeping the production side admin-only.

!!! WARNING
    When generating the key for the productions service account, you are
    responsible to secure it, as it will provide access to Settle production APIs.

See the GCP docs for service accounts
[here](https://cloud.google.com/iam/docs/creating-managing-service-accounts).

To create a project, a service account and its key, use the script below in
Linux or the [GCP console](https://cloud.google.com/shell).

```shell
# project names are unique across GCP, must be between 6 and 30 characters,
#  and may contain only digits, lowercase letters and dashes
#  a typical pattern is {COMPANY}-{PROJECT}-{ENVIRONMENT}
#  e.g. microcorp-project42-sandbox
read PROJECT_ID
SA_NAME="test-service"
gcloud projects create "${PROJECT_ID}"
gcloud iam service-accounts create "${SA_NAME}" --project "${PROJECT_ID}"

# generate service account credentials locally
PATH_TO_SA_PRIVATE_KEY="./sa-private-key.json"
SA_EMAIL="${SA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"
gcloud iam service-accounts keys create "${PATH_TO_SA_PRIVATE_KEY}" \
  --iam-account="${SA_EMAIL}"
```

You may also use the [GCP console](https://console.cloud.google.com/) graphical interface.

!!! TODO
    Create point and click guide for graphical interface.

## Connecting



## Sample client implementation in Python

!!! TODO
    Description

```python
--8<-- "samples/python/client_side.py"
```
