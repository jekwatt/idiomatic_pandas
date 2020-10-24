#!/usr/bin/env python3

import pandas as pd


def records_to_dataframe(records):
    dataframe = pd.DataFrame.from_records(records)
    return dataframe


def dataframe_to_records(dataframe):
    records = dataframe.to_dict("records")
    return records
