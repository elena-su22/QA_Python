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
CREATE VIEW veiw_order_status_change AS SELECT `dst_status_id`,`id`,`order_id`,`scr_status_id`,`time` FROM `order_status_change`;
CREATE VIEW veiw_user AS SELECT `email`,`id`,`name`,`password`,`reg_date` FROM `user`;
