import pytest
import pandas as pd
from utils.plot_tools import generate_data


class Test_plot_tools:
    def test__generate_data(self):
        df = generate_data()
        assert not df.empty
        assert df.__class__ == pd.DataFrame
