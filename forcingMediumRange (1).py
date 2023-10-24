import os
import pytest
from urlgennwm import generate_urls

@pytest.fixture
def generated_urls_for_forcing_medium_range():
    start_date = "202201120000"
    end_date = "202201130000"
    fcst_cycle = [0, 12]
    lead_time = [6, 120]
    varinput = 5
    geoinput = 1
    runinput = 2
    urlbaseinput = 1
    meminput = 1

    generate_urls(start_date, end_date, fcst_cycle, lead_time, varinput, geoinput, runinput, urlbaseinput, meminput)

    yield

def test_generate_urls_for_forcing_medium_range(generated_urls_for_forcing_medium_range):
    assert os.path.exists("filenamelist.txt")
