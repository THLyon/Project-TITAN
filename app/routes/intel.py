from fastapi import APIRouter, BackgroundTasks

router = APIRouter()

@router.post("/enrich")
def kickoff_enrichment(tasks: BackgroundTasks):
    def do_enrich():
        print("Performing background enrichment task...")
    tasks.add_task(do_enrich)
    return {"status": "enrichment started"}