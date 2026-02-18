"""Get currencies from ECB API and calculate their average"""
from ecbdata import ecbdata
import pandas as pd


def import_from_ecb_loop(currencies, start_date):
    """
    Get from ECB currencies and find their averages

    Find from ECB currencies add them to dataframe and below average starting from start_date until current date
    :param currencies: list of currencies
    :param start_date: date from where to start look for currency
    """
    file_to_write = "exchange_rates.md"
    dataframes = {}
    averages = {}

    """Get currency dates"""
    dates_df = (ecbdata.get_series(f'EXR.D.{currencies[0]}.EUR.SP00.A', start=start_date)
                .rename(columns={'TIME_PERIOD': 'DATE'}).filter(['DATE']))

    """Loop through currencies and find their values"""
    for currency in currencies:
        df = (ecbdata.get_series(f'EXR.D.{currency}.EUR.SP00.A', start=start_date)
              .rename(columns={'OBS_VALUE': currency}).filter([currency]))
        dataframes[currency] = df
        averages[currency] = round(df.mean(skipna=True).item(), 4)

    result = pd.concat([dates_df] + list(dataframes.values()), axis=1)
    ave_dict = {'DATE': 'Average'}
    ave_dict.update(averages)
    print(type(ave_dict))
    result = pd.concat([result, pd.DataFrame([ave_dict])], ignore_index=True)
    print(result.to_markdown(index=False))
    """Write result into file"""
    with open(file_to_write, 'wt') as f:
        f.write(f'{result.to_markdown(index=False)}')


if __name__ == '__main__':
    import_from_ecb_loop(['USD', 'SEK', 'GBP', 'JPY'], '2010-01-02')
