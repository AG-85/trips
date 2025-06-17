"""Nearby POI search feature tests."""

import pytest
from pytest_bdd import scenario, given, when, then
import src.trips.app as app

@pytest.fixture
def context():
    return {}

@scenario('trips.feature', 'Find "Area 51" in the search results')
def test_find_area_51_in_the_search_results():
    """Find "Area 51" in the search results."""
    pass

@given('I want to visit "AREA 51"')
def poi_location(context):
    """I want to visit AREA 51."""
    context["location"] = "AREA 51"


@when('I search for "AREA 51"')
def poi_search(context):
    """I search for AREA 51."""
    context["result"] = app.search_nearby_pois(context["location"])


@then('I should see "AREA 51" and related POI\'s in the results')
def result_contains_area_51(context):
    """I should see "AREA 51" and related POI's in the results"."""
    result = context["result"]
    assert "AREA 51" in str(context["result"])

