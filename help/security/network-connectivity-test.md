---
title: Network Connectivity Test
description: Use the Network Connectivity Test in Cloud Manager to validate Advanced Networking and VPN configuration from your program's egress path before you enable networking on environments.
exl-id: a8e44102-5631-4f0c-9de2-1c7b4e8f2d91
feature: Security
role: Admin
---

# Network Connectivity Test {#network-connectivity-test}

The **Network Connectivity Test** is a diagnostic tool in Cloud Manager that helps you confirm that traffic from your program's **Advanced Networking** infrastructure can reach hosts and ports that AEM will use—**before** you enable Advanced Networking on your environments.

Tests run from the **egress side of your Advanced Networking setup** (not from an AEM pod). That path is the same class of network path AEM relies on when Advanced Networking is in use, which makes the tool especially useful for **VPN** scenarios: you can verify DNS, routing, firewalls, and that a service is listening—early in the rollout.

For background on provisioning VPN, dedicated egress IP, or flexible port egress, see [Configuring Advanced Networking for AEM as a Cloud Service](/help/security/configuring-advanced-networking.md).

>[!IMPORTANT]
>
>A successful connectivity test proves that the **network path** from Advanced Networking can reach your target. Your **application code** must still be configured to use the Advanced Networking proxy where required (for example, proxy-related environment variables and port forwarding). If code bypasses the proxy, you may not see traffic from the expected egress path even when the test passes.

## When to use this tool {#when-to-use}

* After **Advanced Networking** is created at the **program** level and **before** or while enabling it on **environments**.
* To validate **VPN** connectivity to customer-managed endpoints (internal hostnames or private IPs).
* To narrow down **DNS** issues versus **firewall or routing** issues when a service does not respond as expected.

>[!NOTE]
>
>This tool is for programs that use Advanced Networking (VPN, dedicated egress IP, or flexible port egress). It is not a general-purpose test of standard AEM connectivity without Advanced Networking.

## Prerequisites {#prerequisites}

* A **non-sandbox** Cloud Manager program.
* **Advanced Networking** infrastructure already created for the program (see [Configuring Advanced Networking](/help/security/configuring-advanced-networking.md)).

## Open the Network Connectivity Test {#open-test}

1. Sign in to Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and open your organization and program.
1. In the program sidebar, go to **Network Infrastructures** (under **Environments**).
1. Either:
   * Select a **network infrastructure** row to open the testing experience, or
   * Open the **row actions** menu (**…**) and choose **Test**.

The **Network Testing** dialog opens.

## Run a test {#run-test}

### Input fields {#input-fields}

| Field | Description | Examples |
| --- | --- | --- |
| **Host** | Hostname or IP address of the service AEM should reach. | `internal-api.example.com`, `10.0.1.50` |
| **Port** | TCP port on the target host (1–65535). Common values may appear in a shortcut list (for example, 80, 443, 587, 22). | `443` |

### Steps {#test-steps}

1. Enter **Host** and **Port**.
1. Select **Test**. Results usually appear within a few seconds.
1. Optional: Use **Copy to clipboard** to capture the full JSON result (useful for support cases).
1. Recent tests may be listed for quick re-runs.

>[!NOTE]
>
>If you enter a **numeric IP** instead of a hostname, DNS resolution is skipped for that value and the IP is used directly.

## Understand the results {#understand-results}

The tool reports several dimensions. Together they describe whether the target is reachable from Advanced Networking and how HTTP-aware checks behaved.

### DNS resolution {#dns-resolution}

| Result | Meaning |
| --- | --- |
| `ips` lists one or more addresses | The hostname resolved successfully using the resolvers associated with your Advanced Networking configuration. |
| DNS error message | Resolution failed (wrong name, resolver not reachable, missing record, and so on). |

**Multiple resolvers:** If your infrastructure defines more than one DNS resolver and they disagree, you may see separate results per resolver so you can spot inconsistent DNS.

### Port open {#port-open}

| Result | Meaning |
| --- | --- |
| **Yes** / true | A TCP connection to the resolved address on the chosen port succeeded. |
| **No** / false | TCP did not connect—port closed, filtered, no listener, or routing/firewall blocked the path. |

### HTTP connectivity {#http-connectivity}

The tool attempts an HTTP/HTTPS-style check on the port (HTTPS first, then HTTP). **Any HTTP status returned by your service** (including redirects, 403, 404, or 5xx) still indicates that a **network path to an HTTP server** responded; the status reflects the application, not Cloud Manager.

| Situation | Meaning |
| --- | --- |
| HTTPS or HTTP success with a status line | The service spoke HTTP(S) on that port. |
| Message such as **Not an HTTP/HTTPS service** | The port may be open, but the service is not speaking HTTP(S) (for example, database, SFTP, custom TCP). Use **Port open** and **Reachability** for these services. |
| **Connection refused** | Nothing is accepting connections on that port. |
| **Connection timed out** | Often firewall or routing; less often severe latency. |
| **No IPs resolved for host** | DNS failed; HTTP check cannot run. |

>[!TIP]
>
>For **non-HTTP** services (for example, databases), expect the HTTP section to show an error or “not HTTP” style outcome. Rely on **Port open** and **Reachability** to confirm connectivity.

### Reachability {#reachability}

| Result | Meaning |
| --- | --- |
| **Reachable** | The host and port are reachable from Advanced Networking for this test. |
| **Unreachable: Port not accessible** | DNS may have worked, but TCP to the port did not succeed. |
| **Unreachable: DNS resolution failed** | The hostname could not be resolved with your configuration. |

## Troubleshooting {#troubleshooting}

### DNS resolution failed {#dns-failed}

1. Confirm the **hostname** (typos and wrong zones are common).
1. Ensure the **DNS servers** configured for Advanced Networking are reachable from the Advanced Networking address space (for VPN, often via the tunnel).
1. Remember that resolution uses **your configured resolvers**, not arbitrary public DNS.
1. For VPN, confirm resolver IPs fall inside **remote networks** that the tunnel actually routes.

### DNS works but the port is not accessible {#dns-ok-port-blocked}

1. On the **target** side, allow traffic from your Advanced Networking **egress** range (and VPN remote CIDRs as applicable).
1. Confirm the **process is listening** on the host and port you tested.
1. For VPN, verify the tunnel, routes, and that the target subnet is reachable through the VPN.
1. Review customer-side **firewall or NSG** rules for the specific port.

### Test shows reachable but AEM does not connect {#reachable-but-aem-fails}

1. Ensure **application code** uses the Advanced Networking **proxy** when required (for example, `AEM_PROXY_HOST` and related settings).
1. Review **port forwarding** at the environment level: `portOrig`, `portDest`, and target host must match how the application connects.
1. Confirm the host is **not** listed under **`nonProxyHosts`**, which would bypass the proxy for that host.

### HTTP shows an error but port is open {#http-error-port-open}

* For **non-HTTP** services, this combination is often **expected**; trust **Port open** and **Reachability**.
* If HTTPS fails but HTTP works, investigate **TLS** configuration or certificate issues on the service.

### Request timeout {#timeout}

* The check is subject to a **short timeout** (on the order of a few seconds). Slow services or high VPN latency can time out.
* Retry once to rule out transient issues.

## Limitations {#limitations}

* The test runs from **Advanced Networking egress infrastructure**, not from an AEM author or publish **pod**.
* It does **not** validate environment-level **port forwarding** rules by themselves—it validates raw reachability from the infrastructure path.
* It does **not** send custom application payloads; HTTP checks use a basic request suitable for diagnostics.
* Typical responses complete in a few seconds; longer waits may hit a **timeout**.

## Related information {#related-information}

* [Configuring Advanced Networking for AEM as a Cloud Service](/help/security/configuring-advanced-networking.md)
* [Advanced networking tutorials on Experience League](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/networking/advanced-networking)
