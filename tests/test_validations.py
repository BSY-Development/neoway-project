from validations.validations import format_name, format_cpf, cpf_validate
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

def test_if_cpf_is_valid():
  assert cpf_validate("222.222.222-22") == False
  assert cpf_validate("123") == False
  assert cpf_validate("178.422.117-11") == False
  assert cpf_validate("01234685744") == True

def test_if_cpf_is_formatted_correcly():
  assert format_cpf("222.222.222-22") == { "formatted": "22222222222", "is_valid": False }
  assert format_cpf("012.346.857-44") == { "formatted": "01234685744", "is_valid": True }
