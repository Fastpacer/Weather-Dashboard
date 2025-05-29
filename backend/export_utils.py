import csv
import json
from fastapi.responses import JSONResponse, StreamingResponse
from io import StringIO, BytesIO
from backend.crud import get_all_queries


def export_as_json():
    data = get_all_queries()
    return JSONResponse(content={"export": data})

def export_as_csv():
    data = get_all_queries()

    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=["location", "type", "timestamp", "data"])
    writer.writeheader()

    for row in data:
        writer.writerow({
            "location": row["location"],
            "type": row["type"],
            "timestamp": row["timestamp"],
            "data": json.dumps(row["data"])  # flatten the dict
        })

    output.seek(0)
    return StreamingResponse(output, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=weather_export.csv"})



