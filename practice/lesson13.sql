SELECT name FROM `good` WHERE count <=100;

SELECT MIN(count) as `мин`, MAX(count) as `макс` FROM `good`;

SELECT AVG(price) AS average_price FROM `good`

ALTER TABLE `good` ADD COLUMN `reaction` VARCHAR(100);
UPDATE `good` SET `reaction` = 'Офигеть цены' WHERE price > 400;
UPDATE `good` SET `reaction` = NULL WHERE price <= 400;

DELETE FROM `good` WHERE `reaction` = NULL; -- неправильная запись, все равно что = 0, а не нет данных
DELETE FROM `good` WHERE `reaction` IS NULL;


-- lesson 14

DROP TABLE order_status

SELECT `email` FROM `user` WHERE `email` LIKE '%gmail%'
SELECT * FROM `user` WHERE `email` LIKE '%gmail%'

SELECT * FROM `user` WHERE BINARY `name` LIKE 'А% М%';
-- = SELECT * FROM `user` WHERE `name` LIKE 'А%' AND `name` LIKE '% М%'

CREATE VIEW veiw_good AS SELECT `id`,`category_id`,`name`,`count`,`price` FROM `good`


CREATE VIEW veiw_good AS SELECT `id`,`category_id`,`name`,`count`,`price` FROM `good`;
CREATE VIEW veiw_good_category AS SELECT `id`,`name`,`parent_id` FROM `good_category`;
CREATE VIEW veiw_order AS SELECT `id`,`status_id`,`user_id`,`creation_date` FROM `order`;
CREATE VIEW veiw_order2good AS SELECT `count`,`good_id`,`order_id` FROM `order2good`;
CREATE VIEW veiw_order_status AS SELECT `code`,`id`,`name`,`sort_index` FROM `order_status`;
CREATE VIEW veiw_order_status_change AS SELECT `dst_status_id`,`id`,`order_id`,`src_status_id`,`time` FROM `order_status_change`;
CREATE VIEW veiw_user AS SELECT `email`,`id`,`name`,`password`,`reg_date` FROM `user`;



CREATE VIEW veiw1 
AS SELECT `good`.`name` AS good_name, `good_category`.`name` AS good_c_name 
FROM `good` 
INNER JOIN `good_category`

CREATE VIEW veiw1 
AS SELECT `good`.`name` AS good_name, `good_category`.`name` AS good_c_name 
FROM `good`
INNER JOIN `good_category` ON good.category_id = good_category.id

CREATE VIEW veiw_good AS SELECT `id`,`category_id`,`name`,`count`,`price` FROM `good`;
CREATE VIEW veiw_order2good AS SELECT `count`,`good_id`,`order_id` FROM `order2good`;

CREATE VIEW veiw2
AS SELECT `good`.`id` AS id_g,`good`.`category_id` AS category_id_g,`good`.`name` AS name_g,`good`.`count` AS count_g,`price` AS price_g,
`order2good`.`count` AS count2, `order2good`.`good_id` AS good_id2, `order2good`.`order_id` AS order_id2
FROM `good`
INNER JOIN `order2good` --вышла ерунда

CREATE VIEW veiw3
AS SELECT `good`.`id` AS id_g,`good`.`category_id` AS category_id_g,`good`.`name` AS name_g,`good`.`count` AS count_g,`good`.`price` AS price_g,
`order2good`.`count` AS count2, `order2good`.`good_id` AS good_id2, `order2good`.`order_id` AS order_id2
FROM `good`
INNER JOIN `order2good` ON `good`.`id` = `order2good`.`good_id`


CREATE VIEW veiw4
AS SELECT `name`, `email`,`reg_date` FROM `user` WHERE `email` LIKE '%gmail%' AND YEAR(`reg_date`) = 2016

CREATE VIEW veiw5
AS SELECT `name`, `email`,DATE_FORMAT(`reg_date`, '%d-%m-%Y') AS `format_date` FROM `user`
WHERE `reg_date` BETWEEN '2015-05-01' AND '2015-06-30';
UPDATE veiw5 SET `name` = 'Человек-1' WHERE `email` LIKE '%com%';
UPDATE veiw5 SET `name` = 'Не-Человек' WHERE `email` NOT LIKE '%com%';

CREATE VIEW user_per_vi_v AS
SELECT
    CASE
        WHEN email LIKE '%.com'THEN 'Человек-1'
        ELSE 'Не-ЧЕЛОВЕК'
    END AS name,email, DATE(reg_date) AS дата
FROM `user`
WHERE reg_date BETWEEN '2015-05-01' AND '2015-06-30' -- как вью5, только с кейс

CREATE VIEW veiw7
AS SELECT `name`,`count`,`price` FROM `good`
WHERE CASE WHEN `name` NOT LIKE 'Айс Ти%' AND `count` < 100 AND `price` > 300 --с кейс не работает =(


CREATE VIEW veiw6
AS SELECT `name`,`count`,`price` FROM `good`
WHERE `name` NOT LIKE 'Айс Ти%' AND `count` < 100 AND `price` > 300 -- без CASE

DELETE FROM `veiw_good` WHERE `name` NOT LIKE '%манго%' --OR `name` NOT LIKE 'манго%' OR `name` NOT LIKE '%манго'



CREATE VIEW veiw7
AS SELECT `id`,`name`,`parent_id` FROM `good_category`
WHERE `name` IS NULL OR `id` IS NULL OR `parent_id` IS NULL;
DELETE FROM `good_category`
WHERE `name` IS NULL OR `id` IS NULL OR `parent_id` IS NULL;
CREATE VIEW veiw8
AS SELECT `id`,`name`,`parent_id` FROM `good_category`
WHERE `name` IS NULL OR `id` IS NULL OR `parent_id` IS NULL;

DROP DATABASE elenasu221 -- Команда "DROP DATABASE" (удалить базу данных) отключена.