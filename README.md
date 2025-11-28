# Project TITAN  
**Threat Intelligence, Triage, and Analysis Node**

---

## Mission Purpose
Project TITAN is an AI-enabled cyber threat fusion platform designed to accelerate the OODA loop (Observe, Orient, Decide, Act) for commanders.  
It ingests, triages, and summarizes cyber threat intelligence feeds in real time, providing actionable recommendations for space, air, terrestrial, and communications domains.

---

## Key Features
- **Multi-Source Ingestion:** Live feeds from CISA KEV, MITRE ATT&CK, NASA, SatNOGS, and malware repositories.  
- **Vector Search:** Historical threat correlation using Pinecone + pgvector (for tactical offline mode).  
- **AI Summaries:** GPT-4o + LLaMA 3 models generate mission-ready executive summaries and defensive COAs.  
- **Threat Prioritization:** Impact scoring aligned to operational relevance (e.g., SATCOM vs. terrestrial comms).  
- **Visualization:** Real-time threat heatmap and attack origin overlays.  

---

## Tech Stack
- **Backend:** Python + FastAPI (with Celery for scheduled ingestion)  
- **Frontend:** React + MUI dashboard  
- **Databases:** PostgreSQL + pgvector, MongoDB for flexible schema storage  
- **Vector Search:** Pinecone (cloud), pgvector (offline deployable)  
- **AI Models:** OpenAI GPT-4o, Hugging Face LLaMA 3, Falcon  
- **Infra:** Docker, Kubernetes (K3s), AWS GovCloud-ready deployment  

---

## Design & Architecture

- [API Notes](docs/API_notes.md)
- [Commander View Mock](docs/commander_view.md)
- [Full Threat Fusion Pipeline](docs/threat_fusion_pipeline.md)
- [High-Level Architecture Diagram](docs/simple_architecture_diagram.md)


---

## Showcase Angle
- Side-by-side **raw intel vs. AI executive summary**.  
- **Live ingestion demo**: pull latest KEV entry in real time.  
- **Threat prioritization view**: command-relevant scoring + heatmap.  
- Framed for integration into **Air Operations Center** or **Space Delta 6** cyber missions.  

---

## Roadmap
- [ ] SIEM integration hooks (Splunk / Elastic).  
- [ ] Expanded space threat feeds.  
- [ ] Role-based access control (RBAC) for multi-team ops.  
- [ ] Automated COA generation with confidence scoring.  





# TITAN – IOC API (Lite Edition)


Small, production‑style FastAPI service for managing IOCs with CRUD, pagination, idempotent bulk upsert, JWT auth (stub), and background enrichment.


## Quickstart


```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
uvicorn app.main:app --reload
```


Open docs at http://127.0.0.1:8000/docs


### Demo credentials
- username: `demo`
- password: `demo123`


### Example
```bash
# Login → JWT
TOKEN=$(curl -sX POST http://127.0.0.1:8000/auth/login -F username=demo -F password=demo123 | jq -r .access_token)


# Bulk upsert
curl -sX POST http://127.0.0.1:8000/iocs/bulkUpsert \
-H "Authorization: Bearer $TOKEN" -H 'Content-Type: application/json' \
-d '[{"type":"ip","value":"1.2.3.4","tags":["abuse"]}, {"type":"domain","value":"bad.example"}]' | jq


# List
curl -s 'http://127.0.0.1:8000/iocs?type=ip&limit=10' -H "Authorization: Bearer $TOKEN" | jq


# Kickoff enrichment (background)
curl -sX POST http://127.0.0.1:8000/intel/enrich \
-H "Authorization: Bearer $TOKEN" -H 'Content-Type: application/json' \
-d '{"ids":[1,2]}' | jq
```


## Notes
- SQLite today; flip DSN in `config.py` to Postgres later (SQLModel/SQLAlchemy 2.0).
- `BackgroundTasks` is fine for demo; use Redis+RQ/Celery for prod with retries/backoff.
- Thin routes → services → repositories; Pydantic I/O models separate from SQLModel tables.
```