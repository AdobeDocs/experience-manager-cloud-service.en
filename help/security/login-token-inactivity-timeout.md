---
title: Login Token Inactivity Timeout Support for Adobe Experience Manager as a Cloud Service
description: Configure inactivity-based (sliding-window) session timeout for the AEM login-token when using encapsulated (JWT) tokens.
feature: Security
role: Admin
---
# Login Token Inactivity Timeout Support for Adobe Experience Manager as a Cloud Service {#login-token-inactivity-timeout-support-for-adobe-experience-manager-as-a-cloud-service}

Adobe Experience Manager issues a `login-token` cookie on successful authentication through the **Adobe Granite Token Authentication Handler**. The handler supports two token modes:

* **Opaque tokens** (default) &mdash; the token is a random value stored in the repository under the user's home. The session is prolonged automatically by the repository as the user stays active.
* **Encapsulated tokens** &mdash; the token is a self-contained, signed (HMAC) JSON Web Token (JWT) that is validated offline, without a repository lookup.

When encapsulated tokens are enabled, you can configure an **inactivity-based (sliding-window) session timeout**: the session stays alive as long as the user keeps making requests, and expires after a configurable period of inactivity.

On AEM as a Cloud Service, the **Author** service is configured to use encapsulated tokens by default. The inactivity timeout settings described here therefore apply to Author without any additional step to enable encapsulated tokens. On other tiers (and on a local AEM SDK Quickstart), encapsulated token support is off by default and must be enabled first.

>[!NOTE]
>
>These settings only take effect when encapsulated token support is enabled (**Enable encapsulated token support** = `true`). When encapsulated token support is disabled, the login-token behaves as before and these settings are ignored.

## How the sliding-window session works {#how-the-sliding-window-session-works}

When **Inactivity Time** is set to a value greater than `0`:

* Each issued login-token is valid for the configured inactivity period (that is, the JWT expires *Inactivity Time* milliseconds after it is issued).
* On each authenticated request, the login-token is renewed &mdash; a fresh token is issued and the updated `login-token` cookie is written to the response &mdash; which extends the session by another inactivity period. This happens transparently, without any user interaction.
* If no request is made within the inactivity period, the token expires and the user must sign in again.
* **Token Renewal Interval** throttles how often the token is renewed, so that a burst of requests does not cause a new token to be issued on every single request.
* An optional **maximum session duration** limits the total lifetime of a session regardless of activity (see [Maximum session duration](#maximum-session-duration)).

When **Inactivity Time** is `0` (the default), the sliding-window behavior is disabled and the login-token keeps its previous behavior.

## Configuration parameters {#configuration-parameters}

The following parameters are configured on the **Adobe Granite Token Authentication Handler** (OSGi configuration `com.day.crx.security.token.impl.impl.TokenAuthenticationHandler`):

| Setting (Web Console label) | OSGi property | Type | Default | Description |
|---|---|---|---|---|
| Enable encapsulated token support | `token.encapsulated` | Boolean | `false` | Enables encapsulated (JWT) tokens, validated offline without repository access. Required for the settings below to take effect. |
| Inactivity Time | `inactivity.time` | Long (milliseconds) | `0` | Maximum period of inactivity before an encapsulated-token session expires. A value greater than `0` enables the sliding-window session; `0` disables it. |
| Token Renewal Interval | `token.renewal.interval` | Long (milliseconds) | `0` | Minimum time between sliding-window token renewals. Prevents a new token from being issued on every request during a burst. Only applies when *Inactivity Time* is greater than `0`; `0` renews on every authenticated request. |
| Skip Login Token Refresh | `skip.token.refresh` | String array | `/libs/granite/csrf/token.json`, `/mnt/overlay/granite/ui/content/shell/header/actions/pulse.data.json` | List of request URIs that must not trigger a sliding-window token renewal. See [Excluding background requests from renewal](#excluding-background-requests-from-renewal). |

### Excluding background requests from renewal {#excluding-background-requests-from-renewal}

Some requests are issued automatically by the AEM UI in the background rather than by an explicit user action &mdash; for example, CSRF token polling (`/libs/granite/csrf/token.json`) and the authoring UI's periodic "pulse" checks. If such requests renewed the login-token, an idle browser tab could keep a session alive indefinitely, defeating the inactivity timeout.

**Skip Login Token Refresh** lists the request URIs that are excluded from sliding-window renewal. A request whose URI matches an entry in this list is still authenticated normally, but it does **not** issue a new token and does **not** reset the inactivity clock. Only genuine user activity on other URIs keeps the session alive.

The default value already covers the common AEM background endpoints. Add your own polling or heartbeat endpoints to the list if they should not count as activity. The value you provide replaces the default, so include the default entries you want to keep.

The corresponding OSGi configuration is a JSON array, for example:

```json
{
  "skip.token.refresh": [
    "/libs/granite/csrf/token.json",
    "/mnt/overlay/granite/ui/content/shell/header/actions/pulse.data.json",
    "/content/mysite/heartbeat.json"
  ]
}
```

>[!NOTE]
>
>This setting only affects sliding-window renewal of encapsulated tokens; it has no effect when *Inactivity Time* is `0`.

### Maximum session duration (absolute cap) {#maximum-session-duration}

In sliding-window mode, the `tokenExpiration` property acts as the **maximum session duration** &mdash; the maximum total lifetime of a session measured from the original sign-in, regardless of activity. Sliding renewal keeps extending the session by the inactivity period, but it can never extend it beyond this cap. Once a session is older than the maximum duration, the token is no longer renewed and the session ends at the next expiry, forcing the user to sign in again.

The maximum session duration is *not* configured on the Token Authentication Handler. It is the `tokenExpiration` property of the **Apache Jackrabbit Oak TokenConfiguration** (OSGi configuration `org.apache.jackrabbit.oak.security.authentication.token.TokenConfigurationImpl`), expressed in milliseconds. Its default is `43200000` (12 hours). A value of `0` disables the cap, so the session can be extended indefinitely as long as the user stays active.

To configure the maximum session duration:

1. Go to the Web Console at `http://serveraddress:serverport/system/console/configMgr`.
1. Search for and click the **Apache Jackrabbit Oak TokenConfiguration**.
1. Set **Token Expiration** (`tokenExpiration`) to the desired maximum session duration, in milliseconds. For example, set it to `28800000` for an 8-hour cap.
1. Click **Save**.
1. Generate and apply the JSON configuration the same way as for the Token Authentication Handler (see [Applying the configuration](#applying-the-configuration)).

The resulting OSGi configuration for an 8-hour maximum session duration looks like this:

```json
{
  "tokenExpiration": 28800000
}
```

>[!NOTE]
>
>Because `tokenExpiration` is a repository-wide setting, it also governs the lifetime of opaque tokens. Choose a value appropriate for both token modes.

## Applying the configuration {#applying-the-configuration}

1. Install a version of the AEM SDK Quickstart locally.
1. Go to the Web Console at `http://serveraddress:serverport/system/console/configMgr`.
1. Search for and click the **Adobe Granite Token Authentication Handler**.
1. Enable **Enable encapsulated token support**, then set **Inactivity Time** and, optionally, **Token Renewal Interval** (both in milliseconds). For example, set **Inactivity Time** to `1800000` for a 30-minute inactivity timeout.
1. Click **Save**.
1. (Optional) To change the absolute session cap, repeat the steps for the **Apache Jackrabbit Oak TokenConfiguration** and set `tokenExpiration`.
1. Generate the JSON format configurations for these settings by following the steps in [Generating OSGi Configurations using the AEM SDK Quickstart](/help/implementing/deploying/configuring-osgi.md#generating-osgi-configurations-using-the-aem-sdk-quickstart).
1. Apply the settings by following the steps in the [Cloud Manager API Format for Setting Properties](/help/implementing/deploying/configuring-osgi.md#cloud-manager-api-format-for-setting-properties) OSGi documentation.

The resulting OSGi configuration for a 30-minute inactivity timeout, renewing at most once per minute, looks like this:

```json
{
  "token.encapsulated": true,
  "inactivity.time": 1800000,
  "token.renewal.interval": 60000
}
```

After the configuration is applied and users sign out and sign in again, `login-token` cookies follow the configured inactivity timeout.
