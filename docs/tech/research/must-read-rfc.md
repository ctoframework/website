# Must-read RFCs

Below is a practical, high impact list of RFCs that most software engineers should at least understand at a conceptual level. They are grouped by area and prioritised for real world relevance.

---

## Core Internet Fundamentals

* **RFC 791** - Internet Protocol (IPv4)
  Foundation of packet routing and addressing.

* **RFC 8200** - Internet Protocol Version 6 (IPv6)
  Modern IP standard.

* **RFC 792** - Internet Control Message Protocol (ICMP)
  Used for ping and network diagnostics.

* **RFC 768** - User Datagram Protocol (UDP)
  Connectionless transport.

* **RFC 9293** - Transmission Control Protocol (TCP consolidation"]
  Reliable transport layer behaviour.

Why it matters: Understanding packet flow, latency, retries, and connection behaviour is essential for debugging distributed systems.

---

## HTTP and Web

* **RFC 9110** - HTTP Semantics
  Methods, status codes, headers, caching rules.

* **RFC 9112** - HTTP/1.1
  Persistent connections, chunked encoding.

* **RFC 7540** - HTTP/2
  Multiplexing, streams, header compression.

* **RFC 6455** - WebSocket Protocol
  Full duplex communication over HTTP.

Why it matters: Every backend, API, or web platform engineer relies on correct HTTP semantics.

---

## DNS

* **RFC 1034** - Domain Names - Concepts and Facilities
* **RFC 1035** - Domain Names - Implementation and Specification

Why it matters: DNS misconfiguration is a frequent cause of outages.

---

## Security and Cryptography

* **RFC 8446** - Transport Layer Security 1.3
  Modern TLS handshake and encryption model.

* **RFC 6749** - OAuth 2.0 Authorization Framework
  Delegated authorisation.

* **RFC 7519** - JSON Web Token
  Token structure and claims.

* **RFC 7617** - Basic HTTP Authentication

Why it matters: Authentication and encryption mistakes are high impact.

---

## Email (Often Overlooked)

* **RFC 5321** - Simple Mail Transfer Protocol
* **RFC 5322** - Internet Message Format

Useful if your product sends email at scale.

---

## Data Formats and APIs

* **RFC 8259** - JavaScript Object Notation (JSON)
* **RFC 3986** - Uniform Resource Identifier

Why it matters: URI encoding and JSON edge cases cause subtle bugs.

---

## Real Time and Networking Extras

* **RFC 5905** - Network Time Protocol Version 4
  Clock synchronisation for distributed systems.

* **RFC 9000** - QUIC Transport Protocol
  Basis of HTTP/3.

---

## If You Build Distributed Systems

* **RFC 1122** - Host Requirements
  Defines host behaviour in TCP/IP stacks.

* **RFC 7234** (Historic but influential) - HTTP caching model
  Now replaced by RFC 9111, but worth understanding historically.

