import os
import pytest
from urlgennwm import generate_urls_operational


@pytest.fixture
def generated_urls_for_analysis_assim_extend():
    start_date = "202201120000"
    end_date = "202201130000"
    fcst_cycle = [16]
    lead_time = [28]
    varinput = 1
    geoinput = 1
    runinput = 6
    urlbaseinput = 2
    meminput = 1
    write_to_file = True

    generate_urls_operational(
        start_date,
        end_date,
        fcst_cycle,
        lead_time,
        varinput,
        geoinput,
        runinput,
        urlbaseinput,
        meminput,
        write_to_file,
    )

    yield


def test_generate_urls_for_analysis_assim_extend(
    generated_urls_for_analysis_assim_extend,
):
    assert os.path.exists("filenamelist.txt")

    expected_urls = [
        "https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/post-processed/WMS/nwm.20220112/analysis_assim_extend/nwm.t16z.analysis_assim_extend.channel_rt.tm028.conus.nc",
        # Add more expected URLs here for the analysis_assim_extend folder
    ]

    with open("filenamelist.txt", "r") as file:
        content = file.read()
        for url in expected_urls:
            assert url in content
