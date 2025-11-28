CISA KEV (Known Exploided Vulnerabilities):
    - No API key
        - CISA exposes KEV as a public JSON feed
    - Official API/Feed: 
        - https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
    - Documentation / KEV homepage: 
        - https://www.cisa.gov/known-exploited-vulnerabilities-catalog

MITRE ATT&CK: 
    - MITRE does not issue API Keys. 
        - They publish data through TAXII server and downloadable JSON/STIX content
    - TAXII Server info: 
        - https://github.com/mitre/cti-taxii-server
    - Official ATT&CK CTI (STIX) - Primary Feed:
        - https://github.com/mitre/cti
    - TAXII root endpoints: 
        - Discovery: https://cti-taxii.mitre.org/taxii
        - Collection URL: https://cti-taxii.mitre.org/stix/

NASA APIs
    - Generate NASA API Key:
        - https://api.nasa.gov/
    - Can request general-purpose key used for: 
        - NeoWS (near-earth objects)
        - Satellite imagery
        - Space weather
        - EPIC
        - Mars rover telemetry
    - DONKI (Database Of Notifications, Knowledge, and Information) - PRIMARY
        - Real-time alerts for: 
            - Solar Flares
            - Geomagnetic Storms
            - CME (Coronal Mass Ejections)
            - SEP (Solar Energetic Particles)
            - Radiation Hazards
            - Magnetospheric Disturbances
            - Satellite Drag Risk
            - GPS degradation conditions
            - High-frequency comms interference
            - Space weather events impacting SATCOM
    - NASA Near-Eartch Object Web Service (NeoWs) - SECONDARY
        - Orbit data
        - Near-Earth object detections
        - Close approach data
        - Potential risk classifications

SatNOGS: read-only intel --> no key needed
    - SatNOGS is open and doesn't require API keys for most usage. 
        - Telemetry, observations, and satellite DB are public
    API Docs (Open, No Key Required): 
        - https://db.satnogs.org/api/
        - https://api.satnogs.org/
    Main Project Site: 
        - https://satnogs.org/
   
Malware Repositories: Varies based on repo
    - MalwareBazaar (absolutely):
        - API key required; log in to generate. 
            - https://bazaar.abuse.ch/api/#api_get_api_key
    - VirusTotal
        - Requires an API key tied to account: 
            - https://www.virustotal.com/gui/my-apikey
    - Malshare: 
        - Free API key after creating an account. 
            - https://malshare.com/register.php
    - MetaDefender (OPSWAT):
        - API key generation: 
            - https://metadefender.opswat.com/apikey