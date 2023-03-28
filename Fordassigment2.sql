-- Nathan Ford 


-- Display the last names of actors and a count of how many actors have the same last name. 
-- Provide in descending order by the counts.
/*
select last_name, count(*) 
from actor 
group by last_name
having count(*) > 1
order by count(*) desc
*/


-- Display the last names of actors and a count of how many actors have the same last name and restrict output by
-- more than 3 actors with the same name. Provide in descending order by the counts first then the last name.

/*
select  count(*), last_name 
from actor
group by last_name
having count(*) < 3
order by count(*) desc
*/

-- Display the first and last names and address of each staff member.
/*
select first_name, last_name, address_id
from staff
*/


-- Display the total payment of each staff member in June of 2005
/*
select SUM (amount), payment_date
from payment
where payment_date between '2005-06-15' and '2005-06-21'
*/

-- Display each film and the number of film actors who are listed for that film. Order the total number of film actors
 -- in descending order.
 /*
select count(actor_id), film_id
from film_actor
group by actor_id
having count(actor_id)>1
order by count(actor_id) desc
*/

-- Display all actors who appear in the film Frisco Forrest using a subquery.
/*
SELECT first_name, last_name
FROM actor
WHERE actor_id IN
(SELECT actor_id
 FROM film_actor
 WHERE film_id =
(SELECT film_id
 FROM film
 WHERE title = 'Frisco Forrest'));
 */
 
 -- Display the most frequently rented movies in descending order. 
/* 
select title, rental_rate 
from film
where rental_rate > 2.5
order by rental_rate desc
*/


-- I have neither given nor received unauthorized aid in completing this work, nor have I presented someone else's work as my own.