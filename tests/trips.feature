Feature: Nearby POI search
  Scenario: Find places within 10 mi
    Given I have hotel coordinates for "San Francisco"
    When I search for nearby places
    Then I should see "10TH STREET MARKET"
