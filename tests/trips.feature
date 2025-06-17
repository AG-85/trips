Feature: Nearby POI search
  Scenario: Find "Area 51" in the search results
    Given I want to visit "AREA 51"
    When I search for "AREA 51"
    Then I should see "AREA 51" and related POI's in the results
