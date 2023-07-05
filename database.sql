CREATE TABLE Users (
  id integer PRIMARY KEY,
  username varchar(255),
  email varchar(255),
  password varchar(255)
);

CREATE TABLE Currencies (
  id integer PRIMARY KEY,
  name varchar(255)
);

CREATE TABLE AlertTypes (
  id integer PRIMARY KEY,
  type varchar(255)
);

CREATE TABLE Alerts (
  id integer PRIMARY KEY,
  currency_id integer,
  value integer,
  user_id integer,
  alert_type_id integer,
  created_at timestamp,
  FOREIGN KEY (currency_id) REFERENCES Currencies (id),
  FOREIGN KEY (user_id) REFERENCES Users (id),
  FOREIGN KEY (alert_type_id) REFERENCES AlertTypes (id)
);

-- ALTER TABLE Alerts ADD FOREIGN KEY (user_id) REFERENCES Users (id);

-- ALTER TABLE Alerts ADD FOREIGN KEY (alert_type_id) REFERENCES AlertTypes (id);

-- ALTER TABLE Alerts ADD FOREIGN KEY (currency_id) REFERENCES Currencies (id);
