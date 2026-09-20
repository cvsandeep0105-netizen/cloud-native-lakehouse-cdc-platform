# Project 02 — Local PostgreSQL CDC Architecture

## Purpose
This document defines the verified local PostgreSQL logical-CDC architecture used as the CDC foundation for Project 02.

## Verified CDC Components
- PostgreSQL 18.4
- wal_level=logical
- Logical replication
- PostgreSQL publication
- PostgreSQL logical replication slot
- pgoutput output plugin
- Replication-capable PostgreSQL role

## Capture Flow
PostgreSQL transaction
? PostgreSQL WAL
? logical decoding
? publication
? logical replication slot
? pgoutput change stream
? CDC consumer
? immutable raw CDC event boundary
? downstream incremental processing

## Area 02 Verification Evidence
Area 02 independently verified genuine PostgreSQL logical CDC.
The controlled test created a PostgreSQL test table and publication, created a logical replication slot, and captured INSERT, UPDATE, and DELETE activity through pgoutput.
The captured evidence is retained under evidence/area-02/cdc.

## Verified Operations
INSERT events were captured successfully.
UPDATE events were captured successfully.
DELETE events were captured successfully.
LSN progression and confirmed flush state were observed during the verification.

## Resource Lifecycle
The Area 02 validation publication and replication slot were removed after testing.
The current baseline therefore contains zero replication slots and zero publications.
CDC infrastructure can be created later when the dedicated implementation requires it.

## Olist Integration Boundary
The Olist files are static historical source data.
They do not directly produce PostgreSQL WAL changes.
To exercise genuine PostgreSQL CDC with Project 02 operational data, controlled changes must first occur in the PostgreSQL operational representation.
Any synthetic historical change stream created for testing must remain explicitly classified as CDC simulation or replay.

## CDC Consumer Boundary
The CDC consumer is a downstream component responsible for reading logical-decoding output and converting it into the Project 02 event representation.
Consumer implementation, event persistence, deduplication, ordering, idempotency, replay, and late-event handling are not claimed as complete by this architecture document.
Those capabilities will be implemented and validated in their dedicated Areas.

## LSN and Ordering
PostgreSQL logical replication provides WAL-derived LSN information that can support deterministic event ordering and checkpointing.
LSN handling must be preserved by the future CDC consumer.
Arrival order alone must not be treated as the authoritative ordering mechanism.

## Failure Boundary
A replication slot retains logical-decoding progress independently of the consumer's application processing.
The consumer must persist or otherwise safely manage its processing checkpoint.
Consumer failures must not silently acknowledge unprocessed events.

## Security Boundary
Replication access must use dedicated least-privilege credentials where possible.
Replication credentials must never be committed to Git.
Replication configuration and secrets must remain environment-specific.

## AWS Boundary
AWS DMS may provide an AWS implementation of source-to-target CDC.
The local PostgreSQL architecture is not evidence of AWS DMS execution.
No AWS CDC runtime performance, availability, or cost is claimed.

## Claim Integrity
Local PostgreSQL logical CDC is verified.
The verification used a controlled test table rather than claiming live CDC from the static Olist distribution.
Future Project 02 CDC implementation must generate its own execution evidence.
