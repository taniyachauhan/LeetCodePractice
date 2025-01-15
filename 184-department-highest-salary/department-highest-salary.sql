# Write your MySQL query statement below


SELECT Department, Employee, salary
FROM
(SELECT d.name as Department, e.salary as salary, e.name as Employee, RANK() OVER (PARTITION BY d.id ORDER BY e.salary DESC) as rnk
FROM Employee e
LEFT JOIN
Department d
on e.departmentId = d.id) t1
WHERE rnk = 1;

