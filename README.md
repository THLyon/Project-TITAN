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

## Architecture Overview
![Architecture Diagram](docs/architecture-diagram.png)

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
