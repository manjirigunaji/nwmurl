import os
import pytest
from urlgennwm import generate_urls

@pytest.fixture
def generated_urls():
    start_date = "202201120000"
    end_date = "202201130000"
    fcst_cycle = [0, 8]
    lead_time = [1, 18]
    varinput = 1
    geoinput = 1
    runinput = 5  # Set to 5 for the analysis_assim folder
    urlbaseinput = 2
    meminput = 1

    generate_urls(start_date, end_date, fcst_cycle, lead_time, varinput, geoinput, runinput, urlbaseinput, meminput)

    yield

def test_generate_urls_for_analysis_assim(generated_urls):
    assert os.path.exists("filenamelist.txt")

    expected_urls = [
        "https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/post-processed/WMS/nwm.20220112/analysis_assim/nwm.t00z.analysis_assim.channel_rt.tm001.conus.nc",
        "https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/post-processed/WMS/nwm.20220112/analysis_assim/nwm.t00z.analysis_assim.channel_rt.tm018.conus.nc",
        # Add more expected URLs here for the analysis_assim folder
    ]

    with open("filenamelist.txt", "r") as file:
        content = file.read()
        for url in expected_urls:
            assert url in content
