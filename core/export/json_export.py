# core/export/json_export.py

import json

def export_user_data(data, path):
    with open(path,"w") as f:
        json.dump(data,f,indent=4)