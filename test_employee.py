
from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name: swathi\n"
        "Employee ID: E304\n"
        "Department: IT\n"
        "Salary: 55000"
    )

    assert employee_details("swathi", "E304", "IT", 55000) == expected_output
