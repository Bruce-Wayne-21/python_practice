-- Solution using DENSE_RANK() window function
CREATE FUNCTION GetNthHighestSalary(@N INT) 
RETURNS INT 
AS
BEGIN
    DECLARE @result INT;
    
    WITH RankedSalaries AS (
        SELECT 
            Salary,
            DENSE_RANK() OVER (ORDER BY Salary DESC) as rank_num
        FROM Employee
    )
    SELECT @result = Salary 
    FROM RankedSalaries 
    WHERE rank_num = @N;
    
    RETURN @result;
END;