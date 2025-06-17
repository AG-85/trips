Feature: Nearby POI search
  Scenario: Find "Area 51" in the search results
    Given I want to visit a location
    When I search for nearby places
    Then I should see "Area 51" in the results"
