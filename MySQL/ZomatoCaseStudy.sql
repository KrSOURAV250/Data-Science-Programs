use zomato;

select count(id) from order_details;

-- replicated sample function from pandas
select * from users order by rand() limit 5;

-- To find the NULL values
SELECT * FROM orders WHERE restaurant_rating = "";
SELECT * FROM orders WHERE restaurant_rating is null;


-- To replace NULL values with 0
-- UPDATE orders SET restaurant_rating = 0 
-- WHERE restaurant_rating IS NULL
select * from users;


-- Q5
select t2.user_id, count(*) as '#order'  from orders t1
join users t2
on t1.user_id = t2.user_id
group by user_id;



-- Q6
select * from restaurants;
select * from menu;

select sum(price) from menu t
group by r_id;

select  r.r_id,  count(r.r_id) from menu m
join restaurants r
on m.r_id = r.r_id
group by r.r_id;



-- Q7
select * from orders;
select r_id, count(r_id) as "No of Votes", avg(restaurant_rating) as "Avg Rating" from orders t where restaurant_rating
group by t.r_id;

-- Q8
select f_name, count(f_id) from menu t1
join food t2
on t1.f_id = t2.f_id
order by count(*) desc limit 1;


-- Q9 -> May
select r_name from restaurants where r_id = (select r_id from orders where month(date) = 5
group by r_id
order by sum(amount)  desc limit 1) ;


-- month by month revenue for a particular restautant = kfc
select month(date), sum(amount)
from orders
where r_id = (select r_id from restaurants where r_name = "kfc")
group by month(date);

-- Q10
select * from (select r_id, sum(amount) as sales from orders 
group by r_id) t having sales > 1500;

-- Q11
select * from users t1
left join orders t2
on t1.user_id = t2.user_id
having t2.order_id is null;

-- Q12
select f_name from (select distinct(t2.f_id) from (select order_id from orders where user_id = 4 and date between "2022-05-15" and "2022-06-15") t1
join order_details t2 where t1.order_id = t2.order_id) t3
join food t4
on t3.f_id = t4.f_id;



-- Q13  pending.......

-- Q14
select r_name, richness from (select r_id, count(f_id) as noOfFood, sum(price)/count(f_id) as richness from menu 
group by r_id
order by richness desc limit 1) t1
join restaurants t2
on t1.r_id = t2.r_id;

-- Q15
select partner_name, salary from (select partner_id, count(partner_id)*100 +1000* avg(delivery_rating) as salary from orders
group by partner_id) t1
join delivery_partner t2
on t1.partner_id = t2.partner_id;


-- Q17  pending..........

-- Q19

select * from restaurants where r_id not in (select r_id from menu where  f_id in (select f_id from food where type = "non-veg"));

-- Q 20
select name, minA , maxA from (select user_id, min(amount) as minA,  max(amount) as maxA from orders
group by user_id) t
join users u
on u.user_id = t.user_id;