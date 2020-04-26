
/* Sample Data from - https://www.naturehills.com/ */

insert into store (store_id, number_of_lots, phone_no, address)
value (1, 10, '9999999999', 'San Jose');
insert into store (store_id, number_of_lots, phone_no, address)
value (2, 20, '8888888888', 'Alameda');
insert into store (store_id, number_of_lots, phone_no, address)
value (3, 30, '7777777777', 'Fresno');
insert into store (store_id, number_of_lots, phone_no, address)
value (4, 30, '6666666666', 'Napa');
insert into store (store_id, number_of_lots, phone_no, address)
value (5, 45, '6666655555', 'Oakland');
insert into store (store_id, number_of_lots, phone_no, address)
value (6, 25, '5555566666', 'Monterey');
insert into store (store_id, number_of_lots, phone_no, address)
value (7, 40, '6666644444', 'Santa Clara');

insert into lot (lot_id, store_id) value (11, 1);
insert into lot (lot_id, store_id) value (12, 1);
insert into lot (lot_id, store_id) value (13, 1);
insert into lot (lot_id, store_id) value (14, 1);
insert into lot (lot_id, store_id) value (15, 1);
insert into lot (lot_id, store_id) value (22, 2);
insert into lot (lot_id, store_id) value (23, 2);
insert into lot (lot_id, store_id) value (24, 2);
insert into lot (lot_id, store_id) value (13, 3);
insert into lot (lot_id, store_id) value (11, 3);
insert into lot (lot_id, store_id) value (41, 4);
insert into lot (lot_id, store_id) value (42, 4);
insert into lot (lot_id, store_id) value (43, 4);
insert into lot (lot_id, store_id) value (44, 4);
insert into lot (lot_id, store_id) value (45, 4);
insert into lot (lot_id, store_id) value (46, 4);



insert into plant_type (type_id, type_name, description) value (90, 'Fruit Trees', 'Backyard orchards with commercial orchard-grade, vigorous fruit trees and bushes');
insert into plant_type (type_id, type_name, description) value (91, 'Holly Bushes', 'Holly is an ancient plant for decoration and ceremonial reasons');
insert into plant_type (type_id, type_name) value (92, 'Privacy Trees');
insert into plant_type (type_id, type_name, description) value (93, 'Flowering Trees',  'Flowering tree for the yard');
insert into plant_type (type_id, type_name, description) value (94, 'Flowering Shrubs', 'To create a beautiful garden design and dramatic presentation');
insert into plant_type (type_id, type_name, description) value (95, 'Patio Trees', 'To add an air of intimacy to an outdoor space');



insert into plant (plant_id, name, price, age, p_type_id) value (200, 'Plum tree', 80, 1, 90);
insert into plant (plant_id, name, price, age, p_type_id) value (201, 'Apple tree', 81, 1, 90);
insert into plant (plant_id, name, price, age, p_type_id) value (202, 'Citrus tree', 82, 1, 90);
insert into plant (plant_id, name, price, age, p_type_id) value (203, 'Fig tree', 80, 1, 90);
insert into plant (plant_id, name, price, age, p_type_id) value (204, 'Pear tree', 82, 1, 90);

insert into plant (plant_id, name, price, age, p_type_id) value (205, 'Yucca', 60, 1, 94);
insert into plant (plant_id, name, price, age, p_type_id) value (206, 'Lilac', 61, 1, 94);
insert into plant (plant_id, name, price, age, p_type_id) value (207, 'Hydrangea', 62, 1, 94);
insert into plant (plant_id, name, price, age, p_type_id) value (208, 'Rose', 60, 1, 94);
insert into plant (plant_id, name, price, age, p_type_id) value (209, 'Bluebeard', 62, 1, 94);
insert into plant (plant_id, name, price, age, p_type_id) value (210, 'Elderberry', 62, 1, 94);
insert into plant (plant_id, name, price, age, p_type_id) value (211, 'Cherry', 60, 1, 94);
insert into plant (plant_id, name, price, age, p_type_id) value (212, 'Forsythia', 62, 1, 94);

insert into plant (plant_id, name, price, age, p_type_id) value (213, 'Crape Myrtle', 30, 1, 95);
insert into plant (plant_id, name, price, age, p_type_id) value (214, 'Topiary', 30, 1, 95);
insert into plant (plant_id, name, price, age, p_type_id) value (215, 'Pink Rose', 32, 1, 95);
insert into plant (plant_id, name, price, age, p_type_id) value (216, 'Mexican Key Lime', 33, 1, 95);
insert into plant (plant_id, name, price, age, p_type_id) value (217, 'Camelliua', 35, 1, 95);
insert into plant (plant_id, name, price, age, p_type_id) value (218, 'Snow Cherry', 35, 1, 95);

insert into plant (plant_id, name, price, age, p_type_id) value (219, 'Fortune Holly Fern', 50, 1, 91);
insert into plant (plant_id, name, price, age, p_type_id) value (220, 'Green Hedge', 51, 2, 92);
insert into plant (plant_id, name, price, age, p_type_id) value (221, 'Japanese Maple', 52, 3, 93);
insert into plant (plant_id, name, price, age, p_type_id) value (222, 'Mademoiselle Holly', 53, 4, 91);




insert into plant_locator value(300, 200, 3, 13);
insert into plant_locator value(301, 201, 3, 11);
insert into plant_locator value(302, 202, 3, 13);
insert into plant_locator value(303, 203, 3, 11);
insert into plant_locator value(304, 205, 3, 13);
insert into plant_locator value(305, 206, 3, 11);
insert into plant_locator value(306, 207, 3, 13);
insert into plant_locator value(307, 208, 3, 11);
insert into plant_locator value(308, 211, 3, 13);
insert into plant_locator value(309, 211, 3, 11);
insert into plant_locator value(310, 206, 3, 13);

insert into plant_locator value(321, 216, 3, 11);
insert into plant_locator value(322, 217, 3, 13);
insert into plant_locator value(323, 213, 3, 11);
insert into plant_locator value(324, 214, 3, 13);
insert into plant_locator value(325, 215, 3, 13);

insert into plant_locator value(311, 201, 1, 12);
insert into plant_locator value(312, 202, 1, 12);
insert into plant_locator value(313, 203, 1, 11);
insert into plant_locator value(314, 205, 1, 13);
insert into plant_locator value(315, 206, 1, 15);
insert into plant_locator value(316, 207, 1, 15);
insert into plant_locator value(317, 208, 1, 11);
insert into plant_locator value(318, 211, 1, 12);
insert into plant_locator value(319, 211, 1, 13);
insert into plant_locator value(320, 206, 1, 11);

insert into plant_locator value(326, 205, 1, 15);
insert into plant_locator value(327, 212, 1, 15);
insert into plant_locator value(328, 206, 1, 11);
insert into plant_locator value(329, 207, 1, 12);
insert into plant_locator value(330, 208, 1, 13);
insert into plant_locator value(331, 210, 1, 11);

insert into plant_locator value(332, 219, 1, 11);
insert into plant_locator value(333, 220, 1, 12);
insert into plant_locator value(334, 221, 1, 13);
insert into plant_locator value(335, 222, 1, 11);