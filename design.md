# Design

An sans-io approach.

## Protocol

The protocol is built on query/response flow.
Application data is is transferred in the query and response frames

Before sending reserved characters should be escaped.


## Connection

The connection should handle application data.
Then pass it to `send()` and receive the bytes with the full query frame to put on the wire.

That means the query object and encryoted query objects are hidden to the user.
