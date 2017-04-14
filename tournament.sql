-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

CREATE TABLE players (
  player_id SERIAL PRIMARY KEY,
  name VARCHAR(20) NOT NULL
);

CREATE TABLE matches (
  match_id SERIAL PRIMARY KEY,
  winner INT REFERENCES players(player_id),
  loser INT REFERENCES players(player_id)
);


-- -- Insert some data into players table
-- INSERT INTO players VALUES (1,'a');
-- INSERT INTO players VALUES (2,'b');
-- INSERT INTO players VALUES (3,'c');

-- -- Insert data into matches table
-- INSERT INTO matches (winner, loser) VALUES (1, 2);
-- INSERT INTO matches (winner, loser) VALUES (3, 2);
-- INSERT INTO matches (winner, loser) VALUES (1, 3);


CREATE VIEW wins AS
  SELECT players.player_id, count(matches.winner) AS num FROM players
  LEFT JOIN matches ON players.player_id = matches.winner
  GROUP BY players.player_id;

CREATE VIEW count AS
  SELECT players.player_id, count(matches.winner) AS num FROM players
  LEFT JOIN matches ON players.player_id = matches.winner
  OR players.player_id = matches.loser
  GROUP BY players.player_id;

CREATE VIEW standings AS
  SELECT players.player_id, players.name, wins.num AS wins, count.num AS matches_played
      FROM players, wins, count
      WHERE players.player_id = wins.player_id and players.player_id = count.player_id
      ORDER BY wins DESC;

