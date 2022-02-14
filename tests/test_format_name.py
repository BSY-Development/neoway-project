from validations.validations import format_name
import pytest

expected = [
  {
    "before": "Miss Cheryl Hughes",
    "after": "CHERYL HUGHES",
  },
  {
    "before": "Mr. Andrew Jordan",
    "after": "ANDREW JORDAN",
  },
  {
    "before": "Clarence Ellis Jr. Sr. I II III IV V MD DDS PhD DVM",
    "after": "CLARENCE ELLIS",
  },
  {
    "before": "Emily Russell",
    "after": "EMILY RUSSELL",
  },
  {
    "before": "Roy Daniels",
    "after": "ROY DANIELS",
  },
]

def test_return_name_formatted_correctly():
  for i in expected:
    assert format_name(i["before"]) == i["after"]

