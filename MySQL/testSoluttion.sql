use insurance;
SELECT * FROM insurances;
-- 1. Show records of 'male' patient from 'southwest' region.
select * from insurances where region = "southwest" and gender = "male";



-- 2. Show all records having bmi in range 30 to 45 both inclusive.
select * from insurances where bmi between 30 and 45;



-- 3. Show minimum and maximum bloodpressure of diabetic patient who smokes. 
-- Make column names as MinBP and MaxBP respectively.
select min(bloodpressure) as MinBP , max(bloodpressure) as MaxBP from insurances where smoker = "yes" and diabetic = "yes";



-- 4. Find no of unique patients who are not from southwest region.
select count(distinct(patientid)) from insurances where region <> "southwest";


-- 5. Total claim amount from male smoker.
select SUM(CLAIM) from insurances where gender = "male" and smoker = "yes";


-- 6. Select all records of south region.
select * from insurances where region like "south%";




-- 7. No of patient having normal blood pressure. Normal range[90-120]
select count(patientid) from insurances where bloodpressure between 90 and 120;



-- 8. No of patient below 17 years of age having normal blood pressure as per below formula -
-- BP normal range = 80+(age in years × 2) to 100 + (age in years × 2)
-- Note: Formula taken just for practice, don't take in real sense.
select  count(patientid) from insurances where age < 17 and bloodpressure between (80 + (age * 2)) and (100 + age * 2);



-- 9. What is the average claim amount for non-smoking female patients 
-- who are diabetic?
select avg(claim) from insurances where gender = "female" and smoker = "no" and diabetic = "yes";


-- 10. Write a SQL query to update the claim amount for the patient 
-- with PatientID = 1234 to 5000.
select * from insurances where patientid = 1234;
update insurances set claim = 5000 where patientid = 1234;
select * from insurances where patientid = 1234;
update insurances set claim = 3500 where patientid = 1234;





-- 11. Write a SQL query to delete all records for patients 
-- who are smokers and have no children.
select * from insurances;
delete from insurances where smoker = "yes" and children = 0;

