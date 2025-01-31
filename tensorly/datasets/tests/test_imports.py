import pytest
from ..data_imports import (
    load_IL2data,
    load_covid19_serology,
    fetch_indian_pines,
    fetch_kinetic,
)


def test_IL2data():
    """Test that data import dimensions match."""
    data = load_IL2data()

    tensor = data["tensor"]
    assert tensor.shape[0] == len(data["ticks"][0])
    assert tensor.shape[1] == len(data["ticks"][1])
    assert tensor.shape[2] == len(data["ticks"][2])
    assert tensor.shape[3] == len(data["ticks"][3])


def test_COVID19_data():
    """Test that data import dimensions match."""
    data = load_covid19_serology()

    tensor = data["tensor"]
    assert tensor.shape[0] == len(data["ticks"][0])
    assert tensor.shape[1] == len(data["ticks"][1])
    assert tensor.shape[2] == len(data["ticks"][2])


@pytest.mark.skip(reason="currently failing, issue #465")
def test_indian_pines():
    """Test that data import dimensions match."""
    data = fetch_indian_pines()

    tensor = data["tensor"]
    assert tensor.shape[0] == len(data["ticks"][0])
    assert tensor.shape[1] == len(data["ticks"][0])
    assert tensor.shape[2] == len(data["ticks"][1])


def test_kinetic():
    """Test that data import dimensions match."""
    data = fetch_kinetic()

    tensor = data["tensor"]
    assert tensor.shape[0] == 64
