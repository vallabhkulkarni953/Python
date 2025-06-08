window.addEventListener('DOMContentLoaded', () => {
  const salary = document.getElementById('salary');
  const salaryOutput = document.getElementById('salaryOutput');
  salaryOutput.value = salary.value;

  const employer_percent = document.getElementById('employer_percent');
  const employerOutput = document.getElementById('employerOutput');
  employerOutput.value = employer_percent.value;

  const employee_percent = document.getElementById('employee_percent');
  const employeeOutput = document.getElementById('employeeOutput');
  employeeOutput.value = employee_percent.value;

  const age = document.getElementById('age');
  const ageOutput = document.getElementById('ageOutput');
  ageOutput.value = age.value;
});
