import os
import pytest
from urlgennwm import generate_urls

@pytest.fixture
def generated_urls():
    start_date = "202310150000"
    end_date = "202310150000"
    fcst_cycle = [0, 8]
    lead_time = [1, 18]
    varinput = 1
    geoinput = 1  # Assuming this is for "conus"
    runinput = 1
    urlbaseinput = 2
    meminput = 1

    generate_urls(start_date, end_date, fcst_cycle, lead_time, varinput, geoinput, runinput, urlbaseinput, meminput)

    yield

def test_generate_urls_for_conus(generated_urls):
    assert os.path.exists("filenamelist.txt")

    # Modify the expected URL to match the "conus" geography
    expected_urls = [
       'https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/post-processed/WMS/nwm.20231015/short_range/nwm.t00z.short_range.channel_rt.f001.conus.nc',
       'https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/post-processed/WMS/nwm.20231015/short_range/nwm.t00z.short_range.channel_rt.f018.conus.nc',
       'https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/post-processed/WMS/nwm.20231015/short_range/nwm.t08z.short_range.channel_rt.f001.conus.nc',
       'https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/post-processed/WMS/nwm.20231015/short_range/nwm.t08z.short_range.channel_rt.f018.conus.nc'
    ]

    with open("filenamelist.txt", "r") as file:
        content = file.read()
        for url in expected_urls:
            assert url in content
