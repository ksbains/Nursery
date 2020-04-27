
/* Sample data referenced from - https://www.naturehills.com/ */

insert into store (store_id, number_of_lots, phone_no, address)
value (1, 10, '9876543211', 'San Jose');
insert into store (store_id, number_of_lots, phone_no, address)
value (2, 20, '9536478264', 'Alameda');
insert into store (store_id, number_of_lots, phone_no, address)
value (3, 30, '9834222647', 'Fresno');
insert into store (store_id, number_of_lots, phone_no, address)
value (4, 30, '8857647343', 'Napa');
insert into store (store_id, number_of_lots, phone_no, address)
value (5, 45, '8945673826', 'Oakland');
insert into store (store_id, number_of_lots, phone_no, address)
value (6, 25, '9998884321', 'Monterey');
insert into store (store_id, number_of_lots, phone_no, address)
value (7, 40, '9845372822', 'Santa Clara');


insert into lot (lot_id, store_id) value (11, 1);
insert into lot (lot_id, store_id) value (12, 1);
insert into lot (lot_id, store_id) value (13, 1);
insert into lot (lot_id, store_id) value (14, 1);
insert into lot (lot_id, store_id) value (15, 1);
insert into lot (lot_id, store_id) value (12, 2);
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
insert into lot (lot_id, store_id) value (51, 5);
insert into lot (lot_id, store_id) value (52, 5);
insert into lot (lot_id, store_id) value (61, 6);
insert into lot (lot_id, store_id) value (62, 6);
insert into lot (lot_id, store_id) value (71, 7);
insert into lot (lot_id, store_id) value (72, 6);


insert into plant_type (type_id, type_name, description) value (90, 'Fruit Trees', 'Backyard orchards with commercial orchard-grade, vigorous fruit trees and bushes');
insert into plant_type (type_id, type_name, description) value (91, 'Holly Bushes', 'Holly is an ancient plant for decoration and ceremonial reasons');
insert into plant_type (type_id, type_name, description) value (92, 'Privacy Trees', 'To block an unsightly view, and assist in noise abatement');
insert into plant_type (type_id, type_name, description) value (93, 'Flowering Trees',  'Flowering tree for the yard');
insert into plant_type (type_id, type_name, description) value (94, 'Flowering Shrubs', 'To create a beautiful garden design and dramatic presentation');
insert into plant_type (type_id, type_name, description) value (95, 'Patio Trees', 'To add an air of intimacy to an outdoor space');


insert into plant (plant_id, name, price, age, p_type_id, description) value (200, 'Plum tree', 80, 1, 90, 'Available European Plum');
insert into plant (plant_id, name, price, age, p_type_id, description) value (201, 'Apple tree', 81, 1, 90, 'Semi dwarf 12-16 inches');
insert into plant (plant_id, name, price, age, p_type_id, description) value (202, 'Citrus tree', 82, 1, 90, 'Available in containers');
insert into plant (plant_id, name, price, age, p_type_id, description) value (203, 'Fig tree', 80, 1, 90, 'Edible fragrant figs');
insert into plant (plant_id, name, price, age, p_type_id, description) value (204, 'Pear tree', 82, 1, 90, 'Bear fruits after 3 years of planting');

insert into plant (plant_id, name, price, age, p_type_id, description) value (205, 'Yucca', 60, 1, 94, 'Red yucca variety');
insert into plant (plant_id, name, price, age, p_type_id, description) value (206, 'Lilac', 61, 1, 94, 'Japanese white variety');
insert into plant (plant_id, name, price, age, p_type_id, description) value (207, 'Hydrangea', 62, 1, 94, 'Reblooming mountain variety');
insert into plant (plant_id, name, price, age, p_type_id, description) value (208, 'Rose', 60, 1, 94, 'Ruby voodoo rose');
insert into plant (plant_id, name, price, age, p_type_id, description) value (209, 'Bluebeard', 62, 1, 94, 'Adaptive to variety of soils');
insert into plant (plant_id, name, price, age, p_type_id, description) value (210, 'Elderberry', 62, 1, 94, 'Edible fall berries');
insert into plant (plant_id, name, price, age, p_type_id, description) value (211, 'Cherry', 60, 1, 94, 'Fairy Tale plant');
insert into plant (plant_id, name, price, age, p_type_id, description) value (212, 'Forsythia', 62, 1, 94, 'Deep yellow variety');

insert into plant (plant_id, name, price, age, p_type_id, description) value (213, 'Crape Myrtle', 30, 1, 95, 'Burgundy foliage variety');
insert into plant (plant_id, name, price, age, p_type_id, description) value (214, 'Topiary', 30, 1, 95, 'Accent evergreen trees');
insert into plant (plant_id, name, price, age, p_type_id, description) value (215, 'Pink Rose', 32, 1, 95, 'Pink blooms');
insert into plant (plant_id, name, price, age, p_type_id, description) value (216, 'Mexican Key Lime', 33, 1, 95, 'Tart fruit with floral hint');
insert into plant (plant_id, name, price, age, p_type_id, description) value (217, 'Camelliua', 35, 1, 95, 'Displays drought tolerance');
insert into plant (plant_id, name, price, age, p_type_id, description) value (218, 'Snow Cherry', 35, 1, 95, 'Fragrant, lovely white spring blooms');

insert into plant (plant_id, name, price, age, p_type_id, description) value (219, 'Fortune Holly Fern', 50, 1, 91, 'Holly-like dark green leaves');
insert into plant (plant_id, name, price, age, p_type_id, description) value (220, 'Green Hedge', 51, 2, 92, 'Red Foliage in Autumn');
insert into plant (plant_id, name, price, age, p_type_id, description) value (221, 'Japanese Maple', 52, 3, 93, 'Greenish Red foliage');
insert into plant (plant_id, name, price, age, p_type_id, description) value (222, 'Mademoiselle Holly', 53, 4, 91, 'Broadleaved Evergreen');

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

insert into plant_locator value(321, 216, 2, 12);
insert into plant_locator value(322, 217, 2, 23);
insert into plant_locator value(323, 213, 2, 12);
insert into plant_locator value(324, 214, 2, 24);
insert into plant_locator value(325, 215, 2, 23);
insert into plant_locator value(311, 201, 2, 12);
insert into plant_locator value(312, 202, 2, 12);
insert into plant_locator value(313, 203, 2, 23);
insert into plant_locator value(314, 205, 2, 24);
insert into plant_locator value(315, 206, 2, 12);


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

insert into plant_locator value(332, 219, 4, 41);
insert into plant_locator value(333, 220, 4, 42);
insert into plant_locator value(334, 221, 4, 43);
insert into plant_locator value(335, 222, 4, 41);
insert into plant_locator value(336, 205, 4, 45);
insert into plant_locator value(337, 212, 4, 45);
insert into plant_locator value(338, 206, 4, 41);
insert into plant_locator value(339, 207, 4, 42);
insert into plant_locator value(340, 208, 4, 43);

insert into plant_locator value(341, 210, 5, 51);
insert into plant_locator value(342, 219, 5, 51);
insert into plant_locator value(343, 220, 5, 52);
insert into plant_locator value(344, 221, 5, 51);
insert into plant_locator value(345, 222, 6, 61);
insert into plant_locator value(346, 206, 6, 61);
insert into plant_locator value(347, 207, 6, 62);
insert into plant_locator value(348, 208, 6, 62);

insert into plant_locator value(349, 200, 1, 12);
insert into plant_locator value(350, 201, 1, 12);
insert into plant_locator value(351, 202, 1, 11);
insert into plant_locator value(352, 213, 1, 11);
insert into plant_locator value(353, 216, 1, 13);
insert into plant_locator value(354, 218, 1, 15);
insert into plant_locator value(356, 219, 1, 12);
insert into plant_locator value(357, 220, 1, 13);
insert into plant_locator value(358, 221, 1, 14);
insert into plant_locator value(359, 222, 1, 12);
