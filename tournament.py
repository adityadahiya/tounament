# tournament.py -- implementation of a Swiss-system tournament

import psycopg2


def connect(database_name="tournament"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("<error message>")

def deleteMatches():
    """Remove all the match records from the database."""
    db,cursor = connect()
    cur = db.cursor()
    cur.execute("DELETE FROM matches;")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db,cursor = connect()
    cur = db.cursor()
    cur.execute("TRUNCATE players CASCADE;")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db,cursor = connect()
    cur = db.cursor()
    cur.execute("SELECT count(*) AS num FROM players;")
    player_count = cur.fetchone()
    db.close()
    return player_count[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db,cursor = connect()
    cur = db.cursor()
    query = "INSERT INTO players (name) VALUES (%s);"
    params = (name,)
    cur.execute(query,params)
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db,cursor = connect()
    cur = db.cursor()
    cur.execute("SELECT * FROM standings")
    player_standings = cur.fetchall()
    db.close()

    return player_standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db,cursor = connect()
    cur = db.cursor()
    cur.execute("""
        INSERT INTO matches (winner, loser) VALUES
        (%s,%s)""",(winner, loser,))
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    db,cursor= connect()
    cur = db.cursor()
    query = "SELECT * FROM standings"
    cur.execute(query)
    results = cur.fetchall()
    pairings = []
    count = len(results)
    for x in range(0, count - 1, 2):
        paired_list = (results[x][0], results[x][1], results[x + 1][0], results[x + 1][1])
        pairings.append(paired_list)

    db.close()
    return pairings
