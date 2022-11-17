import pandas as pd
from datetime import datetime

def load_data(filename):
    return pd.read_csv(filename)


def transform(sakibase) -> pd.DataFrame:
    sakibase['time'] = sakibase['time'].apply(lambda x: datetime.strptime(x, r'%Y-%m-%d %H:%M'))
    sakibase['date'] = sakibase['time'].apply(lambda x: x.date())
    return sakibase
