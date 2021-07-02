import pandas as pd
import numpy as np
from yahoo_finance import Share

yahoo = Share('YHOO')

print(yahoo.get_price())

