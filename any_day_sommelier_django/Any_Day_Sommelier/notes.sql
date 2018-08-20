

ERD-----------------

CREATE TABLE wine (
  id SERIAL PRIMARY KEY,
  type VARCHAR(32)
);

CREATE TABLE food (
  id SERIAL PRIMARY KEY,
  entree VARCHAR(64),
  main_ingredient VARCHAR(64)
);

CREATE TABLE user (
  id SERIAL PRIMARY KEY,
  email VARCHAR(64),
  password VARCHAR(32)
);

CREATE TABLE pairing (
  id SERIAL PRIMARY KEY, 
  wine_id INTEGER REFERENCES wine(id), 
  food_id INTEGER REFERENCES food(id)  
);

CREATE TABLE favorites (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES user(id),
  pairing_id INTEGER REFERENCES pairing(id)
);




ROUTES------------------


/                 GET         index         Home
*/pairing          GET         index         Index of all pairings
*/wine/:id         GET         show          Show individual wine - and which entrees it goes with
*/wine             GET         index         Index of all wines
*/food/:id         GET         show          Show individual dish - and wines it goes with
*/food             GET         index         Index all dishes
/auth             POST        create        Create new user
/auth/:id         GET         show          View user profile - including their liked pairings
/auth/:id         DELETE      destroy       Destroy account
/auth/:id/edit    PUT         update        update profile -- would this be for adding a pairing to favorites?
/upvote?
/downvote?