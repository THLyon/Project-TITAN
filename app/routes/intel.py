from fastapi import APIRouter, BackgrountTasks

router = APIRouter()

@router.post("/enrich")
def kickoff_enrichment(tasks: BackgrountTasks):
    def do_enrich():
        print("Performing background enrichment task...")
    tasks.add_task(do_enrich)
    return {"status": "enrichment started"}