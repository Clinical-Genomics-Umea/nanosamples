import pandas as pd
from pathlib import Path
import yaml


def import_ws(file: Path, tr_fields: dict, dtypes: dict, model_fields: dict, sample_defaults: dict) -> pd.DataFrame:
    fields = list(model_fields.keys())
    df_empty = pd.DataFrame(columns=fields)
    df = pd.read_csv(file, sep=';',
                     dtype={'Prov ID': 'object'})
    df = df.rename(columns=tr_fields)
    df_complete = pd.concat([df_empty, df])
    df_complete.dropna(subset=['internal_lab_id'], inplace=True)
    for field, value in sample_defaults.items():
        print(field, type(value))
        if value != "None":
            df_complete[field] = value

    for field in model_fields:
        dtype = model_fields[field]['dtype']
        df_complete[field] = df_complete[field].astype(dtype)

    return df_complete


def load_yaml(file: Path) -> dict:
    with open(file, "r", encoding='utf-8') as fh:
        return yaml.safe_load(fh)
