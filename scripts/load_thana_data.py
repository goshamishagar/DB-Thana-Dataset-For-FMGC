"""Bangladesh Thana Dataset — Quick Start Loader | github.com/shagargoshami"""
import pandas as pd, os
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

def load_all():
    keys = ["Division", "District", "Thana / Upazila"]
    t = pd.read_csv(os.path.join(DATA_DIR, "thana_reference.csv"))
    e = pd.read_csv(os.path.join(DATA_DIR, "thana_economic_activity.csv"))
    p = pd.read_csv(os.path.join(DATA_DIR, "thana_fmcg_consumer_profile.csv"))
    return t.merge(e, on=keys).merge(p, on=keys)

if __name__ == "__main__":
    df = load_all()
    print(f"Loaded {len(df)} thanas | {df['Division'].nunique()} divisions | {df['District'].nunique()} districts")
    print(df["Distribution Priority"].value_counts())
