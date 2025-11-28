   [Sensors & Feeds]
       |   |   |   |
       |   |   |   +-- SatNOGS RF Anomaly
       |   |   +------ NASA GNSS / Space Alerts
       |   +---------- Malware Repos (hashes, IOCs)
       +--------------- CISA KEV, MITRE ATT&CK
                           |
                           v
                  [Ingestion API Layer]
                           |
                  - Transformers / Parsers
                  - CVE Normalizer
                  - TTP Mapper
                           |
                           v
               [Semantic Enrichment Pipeline]
                  - LLM entity extraction
                  - Threat tagging (APT? region?)
                  - Attack chain mapping
                           |
                           v
              [Threat Correlation Graph Engine]
       Links: CVE → ATT&CK Tactic → Malware → Domain → Campaign
                           |
                           v
                   [Vector Embedding Layer]
                  - Pinecone online mode
                  - pgvector offline tactical mode
                           |
                           v
               [Mission-Oriented Prioritizer]
       Inputs:
       - Operational domain (SATCOM, Air Ops, Ground)
       - Asset criticality
       - Real-time telemetry risk
       - Exploitation likelihood
                           |
                           v
                     [AI Decision Layer]
                  GPT-4o / LLaMA-3 produce:
                  - Executive summaries
                  - Technical briefs
                  - COAs
                  - Urgency rating
                           |
                           v
                    [TITAN UI + API]
