import pandas as pd

data = {
    "Country Name": ["Angola", "Argentina", "Armenia", "Australia", "Ireland"],
    "Country Code": ["AGO", "ARG", "ARM", "AUS", "IRL"],
    "2019": [2142.238757, 9963.672506, 4828.505178, 54941.43418, 80927.07467],
    "2020": [1603.993477, 8496.424142, 4505.867364, 51720.37076, 85420.19086],
    "2021": [1953.533757, 10636.1202, 4966.513471, 60443.10916, 100172.0793]
}

df = pd.DataFrame(data)
print(df)
