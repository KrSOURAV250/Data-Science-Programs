-- USE zomato
-- SELECT COUNT(*) FROM order_details

-- replicated sample function from pandas
-- SELECT * FROM users ORDER BY rand() LIMIT 5

-- To find the NULL values
-- SELECT * FROM orders WHERE restaurant_rating IS NULL

-- To replace NULL values with 0
-- UPDATE orders SET restaurant_rating = 0 
-- WHERE restaurant_rating IS NULL

-- Q5 uh


-- Q6


-- Q7


-- Q8


-- Q9 -> May
-- SELECT MONTHNAME(DATE(date)),date FROM orders


-- month by month revenue for a particular restautant = kfc


-- Q10


-- Q11


-- Q12


-- Q13


-- Q14


-- Q15


-- Q17
-- SELECT CORR(delivery_time,delivery_rating) AS 'corr'
-- FROM orders;

-- Q19


-- Q 20
SELECT name,MIN(amount),MAX(amount),AVG(amount) FROM orders t1
JOIN users t2
ON t1.user_id = t2.user_id
GROUP BY t1.user_id


