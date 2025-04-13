# HATEOAS

HATEOAS—**Hypermedia As The Engine Of Application State**—is a constraint of the REST application architecture. It ensures that a client interacts with a REST API entirely through hyperlinks provided dynamically by the server. The client doesn't need to hardcode or guess resource URIs; instead, it follows links contained in responses to navigate and perform actions.

Imagine a user interface that adapts based on a user's permissions. Instead of exposing all possible actions upfront, the UI renders only what’s available to that specific user in that specific state. HATEOAS does the same for APIs: the server includes relevant links in each response, guiding the client on what can be done next.

### Why it matters:

- **Decoupling**: Clients don’t need to be updated when URIs or workflows change, as long as they keep following the links.
- **Discoverability**: APIs become self-descriptive. Clients can dynamically explore capabilities without prior knowledge.
- **Adaptability**: Logic about available actions is centralised on the server, allowing dynamic control based on state, roles, or context.

### A simple example:

A `GET /orders/123` response might include:

```json
{
  "id": 123,
  "status": "processing",
  "links": [
    { "rel": "cancel", "method": "POST", "href": "/orders/123/cancel" },
    { "rel": "track", "method": "GET", "href": "/orders/123/tracking" }
  ]
}
```

The client doesn’t need to know in advance what actions are possible—it simply follows the links.

HATEOAS brings flexibility, resilience, and clarity to API design, encouraging smarter, more maintainable client-server interactions.
