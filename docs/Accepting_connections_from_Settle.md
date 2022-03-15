!!! IMPORTANT
    Your API must be exposed the internet.

    Settle no longer uses VPN for securing communication for new integrations.

In this scenario, the *Client Service* is a Settle service and the *API Server*
is your API server.

Settle will provide you with one *service account email* for each Settle service
that needs to access your server. You must register the email in your system.
Typically, there will be a single Settle service that will need to be registered.

When connecting to your API server,
Settle will transmit the token as part of the request headers
in the `Authorization: Bearer <TOKEN>` form.

You will use a GCP Auth Server to verify the token included in the request is valid.
Then you will verify that the decoded token contents contain the
Settle *service account email* and the endpoint URL as the *audience*.

To perform the verifications you need to implement code in your API server.
This effort should be minimal if you use the appropriate Google client library.

We have included links for several languages in the [Reference](#reference) section.

## Sample server implementation in Python

!!! TODO
    Description

```python
--8<-- "samples/python/server_side.py"
```
