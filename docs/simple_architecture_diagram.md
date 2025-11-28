                    +---------------------------+
                    |       External Feeds      |
                    |---------------------------|
                    | - CISA KEV                |
                    | - MITRE ATT&CK            |
                    | - NASA Cyber Alerts       |
                    | - SatNOGS Telemetry       |
                    | - Malware Repositories    |
                    +--------------+------------+
                                   |
                                   v
                     +---------------------------+
                     |   Ingestion Layer (ETL)   |
                     |---------------------------|
                     | - Scheduled Polling       |
                     | - Webhooks (where avail.) |
                     | - Parsing / Normalizing   |
                     +--------------+------------+
                                   |
                                   v
           +-----------------------------------------------------+
           |                   Fusion Core                        |
           |-----------------------------------------------------|
           |  A. Threat Correlation Engine                       |
           |     - CVE ↔ ATT&CK ↔ Malware ↔ Telemetry            |
           |                                                     |
           |  B. Vector Search (Pinecone + pgvector offline)     |
           |     - Similar incidents                             |
           |     - Past campaigns                                |
           |                                                     |
           |  C. AI Analysis                                     |
           |     - GPT-4o Executive Summaries                    |
           |     - LLaMA-3 Technical Deep Dives                  |
           |     - COA (Course of Action) Output                 |
           |                                                     |
           |  D. Mission Prioritization Engine                   |
           |     - Space / Air / Ground scoring                  |
           |     - Critical-system impact analysis               |
           +-------------+---------------------------------------+
                         |
                         v
              +----------------------------+
              |     Data Storage Layer     |
              |----------------------------|
              | - Postgres for structured  |
              | - Pinecone for embeddings  |
              | - S3 for raw artifacts     |
              +-------------+--------------+
                            |
                            v
              +----------------------------+
              |      TITAN Command UI      |
              |----------------------------|
              | - Threat Heatmap           |
              | - Live Alerts Pane         |
              | - Impact Scores            |
              | - OODA Summary             |
              | - Search / Vector Query     |
              +----------------------------+
