Make sure you download the starter code and run the following:

```sh
  psql < movies.sql
  psql movies_db
```

In markdown, you can place a code block inside of three backticks (```) followed by the syntax highlighting you want, for example

\```sql

SELECT \* FROM users;

\```

Using the `movies_db` database, write the correct SQL queries for each of these tasks:

1.  The title of every movie.

Star Wars: The Force Awakens
 Marvel's The Avengers
 Star Wars: The Last Jedi
 Black Panther
 Rogue One: A Star Wars Story
 Beauty and the Beast
 Finding Dory
 Avengers: Age of Ultron
 Pirates of the Caribbean: Dead Man's Chest
 The Lion King
 Avatar
 Star Wars: Episode I - The Phantom Menace
 Star Wars
 Star Wars: Episode III - Revenge of the Sith
 Deadpool
 Star Wars: Episode II - Attack of the Clones
 Return of the Jedi
 Independence Day
 The Empire Strikes Back
 Home Alone
 Titanic
 Transformers: Revenge of the Fallen
 Transformers: Dark of the Moon
 Forrest Gump
 Shrek the Third
 Transformers
 Iron Man
 Indiana Jones & Kingdom of the Crystal Skull
 Iron Man 2
 Jurassic World
 E. T.: The Extra-Terrestrial
 Jurassic Park
 The Secret Life of Pets
 Despicable Me 2
 Furious 7
 Minions
 Meet the Fockers
 Sing
 Despicable Me 3
 The Dark Knight
 The Dark Knight Rises
 Wonder Woman
 Harry Potter and the Deathly Hallows: Part 2
 American Sniper
 Batman v Superman: Dawn of Justice
 It
 Suicide Squad
 Harry Potter and the Sorcerer's Stone
 The Hobbit: An Unexpected Journey
 Harry Potter and the Half-Blood Prince
 Harry Potter and the Deathly Hallows: Part 1
 Inception
 Harry Potter and the Order of the Phoenix
 Man of Steel
 The Matrix Reloaded
 Shrek 2
 Shrek
 The Hunger Games: Catching Fire
 The Hunger Games
 The Hunger Games: Mockingjay - Part 1
 The Twilight Saga: Breaking Dawn Part 2
 The Hunger Games: Mockingjay - Part 2
 Spider-Man
 Jumanji: Welcome to the Jungle
 Spider-Man 2
 Spider-Man 3
 Spider-Man: Homecoming
 Skyfall
 The Amazing Spider-Man
 The Lord of the Rings: Return of the King
 The Lord of the Rings: The Two Towers
 The Lord of the Rings: Fellowship of the Ring
 The Passion of the Christ
 The Twilight Saga: Eclipse
 The Twilight Saga: New Moon
 The Twilight Saga: Breaking Dawn Part 1
 Toy Story 3
 Iron Man 3
 Captain America: Civil War
 Frozen
 Guardians of the Galaxy Vol. 2
 Finding Nemo
 The Jungle Book
 Inside Out
 Zootopia
 Alice in Wonderland
 Guardians of the Galaxy
 Thor: Ragnarok
 Pirates of the Caribbean: At World's End
 Pirates of the Caribbean: Curse of the Black Pearl
 The Sixth Sense
 Up
 The Chronicles of Narnia: Lion, Witch & Wardrobe
 Monsters, Inc.
 Monsters University
 The Incredibles
 Toy Story 2
 Harry Potter and the Goblet of Fire
 The Hangover
 Gravity
 Harry Potter and the Chamber of Secrets

2.  All information on the G-rated movies.

 id  |        title        | release_year | runtime | rating | studio_id 
-----+---------------------+--------------+---------+--------+-----------
  20 | The Lion King       |         1994 |      89 | G      |         1
  21 | Toy Story 3         |         2010 |     103 | G      |         1
  33 | Finding Nemo        |         2003 |     104 | G      |         1
  86 | Monsters, Inc.      |         2001 |      90 | G      |         1
  95 | Monsters University |         2013 |     107 | G      |         1
 101 | Toy Story 2         |         1999 |      95 | G      |         1

3.  The title and release year of every movie, ordered with the
    oldest movie first.
    
                       title                        | release_year 
----------------------------------------------------+--------------
 Star Wars                                          |         1977
 The Empire Strikes Back                            |         1980
 E. T.: The Extra-Terrestrial                       |         1982
 Return of the Jedi                                 |         1983
 Home Alone                                         |         1990
 Jurassic Park                                      |         1993
 The Lion King                                      |         1994
 Forrest Gump                                       |         1994
 Independence Day                                   |         1996
 Titanic                                            |         1997
 The Sixth Sense                                    |         1999
 Star Wars: Episode I - The Phantom Menace          |         1999
 Toy Story 2                                        |         1999
 Harry Potter and the Sorcerer's Stone              |         2001
 Monsters, Inc.                                     |         2001
 The Lord of the Rings: Fellowship of the Ring      |         2001
 Shrek                                              |         2001
 Harry Potter and the Chamber of Secrets            |         2002
 The Lord of the Rings: The Two Towers              |         2002
 Star Wars: Episode II - Attack of the Clones       |         2002
 Spider-Man                                         |         2002
 Finding Nemo                                       |         2003
 Pirates of the Caribbean: Curse of the Black Pearl |         2003
 The Lord of the Rings: Return of the King          |         2003
 The Matrix Reloaded                                |         2003
 The Passion of the Christ                          |         2004
 Spider-Man 2                                       |         2004
 Meet the Fockers                                   |         2004
 The Incredibles                                    |         2004
 Shrek 2                                            |         2004
 Harry Potter and the Goblet of Fire                |         2005
 The Chronicles of Narnia: Lion, Witch & Wardrobe   |         2005
 Star Wars: Episode III - Revenge of the Sith       |         2005
 Pirates of the Caribbean: Dead Man's Chest         |         2006
 Shrek the Third                                    |         2007
 Transformers                                       |         2007
 Harry Potter and the Order of the Phoenix          |         2007
 Spider-Man 3                                       |         2007
 Pirates of the Caribbean: At World's End           |         2007
 Indiana Jones & Kingdom of the Crystal Skull       |         2008
 The Dark Knight                                    |         2008
 Iron Man                                           |         2008
 Transformers: Revenge of the Fallen                |         2009
 The Hangover                                       |         2009
 Up                                                 |         2009
 Avatar                                             |         2009
 Harry Potter and the Half-Blood Prince             |         2009
 The Twilight Saga: New Moon                        |         2009
 The Twilight Saga: Eclipse                         |         2010
 Toy Story 3                                        |         2010
 Harry Potter and the Deathly Hallows: Part 1       |         2010
 Inception                                          |         2010
 Iron Man 2                                         |         2010
 Alice in Wonderland                                |         2010
 Harry Potter and the Deathly Hallows: Part 2       |         2011
 Transformers: Dark of the Moon                     |         2011
 The Twilight Saga: Breaking Dawn Part 1            |         2011
 The Amazing Spider-Man                             |         2012
 The Dark Knight Rises                              |         2012
 The Twilight Saga: Breaking Dawn Part 2            |         2012
 The Hobbit: An Unexpected Journey                  |         2012
 Marvel's The Avengers                              |         2012
 The Hunger Games                                   |         2012
 Skyfall                                            |         2012
 Man of Steel                                       |         2013
 Monsters University                                |         2013
 The Hunger Games: Catching Fire                    |         2013
 Iron Man 3                                         |         2013
 Gravity                                            |         2013
 Frozen                                             |         2013
 Despicable Me 2                                    |         2013
 The Hunger Games: Mockingjay - Part 1              |         2014
 Guardians of the Galaxy                            |         2014
 American Sniper                                    |         2014
 Star Wars: The Force Awakens                       |         2015
 Furious 7                                          |         2015
 Jurassic World                                     |         2015
 The Hunger Games: Mockingjay - Part 2              |         2015
 Inside Out                                         |         2015
 Avengers: Age of Ultron                            |         2015
 Minions                                            |         2015
 Deadpool                                           |         2016
 The Jungle Book                                    |         2016
 Zootopia                                           |         2016
 The Secret Life of Pets                            |         2016
 Suicide Squad                                      |         2016
 Sing                                               |         2016
 Batman v Superman: Dawn of Justice                 |         2016
 Finding Dory                                       |         2016
 Rogue One: A Star Wars Story                       |         2016
 Captain America: Civil War                         |         2016
 Star Wars: The Last Jedi                           |         2017
 Guardians of the Galaxy Vol. 2                     |         2017
 Despicable Me 3                                    |         2017
 Beauty and the Beast                               |         2017
 Spider-Man: Homecoming                             |         2017
 It                                                 |         2017
 Wonder Woman                                       |         2017
 Thor: Ragnarok                                     |         2017
 Jumanji: Welcome to the Jungle                     |         2018
 Black Panther
    
4.  All information on the 5 longest movies.

id |                     title                     | release_year | runtime | rating | studio_id 
----+-----------------------------------------------+--------------+---------+--------+-----------
 35 | The Lord of the Rings: Return of the King     |         2003 |     200 | PG-13  |         9
  3 | Titanic                                       |         1997 |     194 | PG-13  |         3
 46 | The Lord of the Rings: The Two Towers         |         2002 |     179 | PG-13  |         9
 63 | The Lord of the Rings: Fellowship of the Ring |         2001 |     178 | PG-13  |         9
 67 | Pirates of the Caribbean: At World's End      |         2007 |     168 | PG-13  |         1

5.  A query that returns the columns of `rating` and `total`, tabulating the
    total number of G, PG, PG-13, and R-rated movies.
    
 rating | total 
--------+-------
 PG-13  |    64
 R      |     6
 G      |     6
 PG     |    25

6.  A table with columns of `release_year` and `average_runtime`,
    tabulating the average runtime by year for every movie in the database. The data should be in reverse chronological order (i.e. the most recent year should be first).

release_year |   average_runtime    
--------------+----------------------
         2018 | 129.5000000000000000
         2017 | 130.7500000000000000
         2016 | 118.3000000000000000
         2015 | 122.8571428571428571
         2014 | 125.3333333333333333
         2013 | 117.4285714285714286
         2012 | 144.2857142857142857
         2011 | 130.6666666666666667
         2010 | 126.5000000000000000
         2009 | 129.8333333333333333
         2008 | 132.0000000000000000
         2007 | 136.4000000000000000
         2006 | 151.0000000000000000
         2005 | 143.6666666666666667
         2004 | 115.0000000000000000
         2003 | 144.2500000000000000
         2002 | 148.2500000000000000
         2001 | 127.7500000000000000
         1999 | 111.6666666666666667
         1997 | 194.0000000000000000
         1996 | 153.0000000000000000
         1994 | 115.0000000000000000
         1993 | 127.0000000000000000
         1990 | 105.0000000000000000
         1983 | 134.0000000000000000
         1982 | 117.0000000000000000
         1980 | 129.0000000000000000
         1977 | 121.0000000000000000

7.  The movie title and studio name for every movie in the
    database.
    
                        title                        |             studio_name             
----------------------------------------------------+-------------------------------------
 Star Wars: The Force Awakens                       | Walt Disney Studios Motion Pictures
 Marvel's The Avengers                              | Walt Disney Studios Motion Pictures
 Star Wars: The Last Jedi                           | Walt Disney Studios Motion Pictures
 Black Panther                                      | Walt Disney Studios Motion Pictures
 Rogue One: A Star Wars Story                       | Walt Disney Studios Motion Pictures
 Beauty and the Beast                               | Walt Disney Studios Motion Pictures
 Finding Dory                                       | Walt Disney Studios Motion Pictures
 Avengers: Age of Ultron                            | Walt Disney Studios Motion Pictures
 Pirates of the Caribbean: Dead Man's Chest         | Walt Disney Studios Motion Pictures
 The Lion King                                      | Walt Disney Studios Motion Pictures
 Avatar                                             | 20th Century Fox
 Star Wars: Episode I - The Phantom Menace          | 20th Century Fox
 Star Wars                                          | 20th Century Fox
 Star Wars: Episode III - Revenge of the Sith       | 20th Century Fox
 Deadpool                                           | 20th Century Fox
 Star Wars: Episode II - Attack of the Clones       | 20th Century Fox
 Return of the Jedi                                 | 20th Century Fox
 Independence Day                                   | 20th Century Fox
 The Empire Strikes Back                            | 20th Century Fox
 Home Alone                                         | 20th Century Fox
 Titanic                                            | Paramount Pictures
 Transformers: Revenge of the Fallen                | Paramount Pictures
 Transformers: Dark of the Moon                     | Paramount Pictures
 Forrest Gump                                       | Paramount Pictures
 Shrek the Third                                    | Paramount Pictures
 Transformers                                       | Paramount Pictures
 Iron Man                                           | Paramount Pictures
 Indiana Jones & Kingdom of the Crystal Skull       | Paramount Pictures
 Iron Man 2                                         | Paramount Pictures
 Jurassic World                                     | Universal Pictures
 E. T.: The Extra-Terrestrial                       | Universal Pictures
 Jurassic Park                                      | Universal Pictures
 The Secret Life of Pets                            | Universal Pictures
 Despicable Me 2                                    | Universal Pictures
 Furious 7                                          | Universal Pictures
 Minions                                            | Universal Pictures
 Meet the Fockers                                   | Universal Pictures
 Sing                                               | Universal Pictures
 Despicable Me 3                                    | Universal Pictures
 The Dark Knight                                    | Warner Bros.
 The Dark Knight Rises                              | Warner Bros.
 Wonder Woman                                       | Warner Bros.
 Harry Potter and the Deathly Hallows: Part 2       | Warner Bros.
 American Sniper                                    | Warner Bros.
 Batman v Superman: Dawn of Justice                 | Warner Bros.
 It                                                 | Warner Bros.
 Suicide Squad                                      | Warner Bros.
 Harry Potter and the Sorcerer's Stone              | Warner Bros.
 The Hobbit: An Unexpected Journey                  | Warner Bros.
 Harry Potter and the Half-Blood Prince             | Warner Bros.
 Harry Potter and the Deathly Hallows: Part 1       | Warner Bros.
 Inception                                          | Warner Bros.
 Harry Potter and the Order of the Phoenix          | Warner Bros.
 Man of Steel                                       | Warner Bros.
 The Matrix Reloaded                                | Warner Bros.
 Shrek 2                                            | Dreamworks SKG
 Shrek                                              | Dreamworks SKG
 The Hunger Games: Catching Fire                    | Lionsgate
 The Hunger Games                                   | Lionsgate
 The Hunger Games: Mockingjay - Part 1              | Lionsgate
 The Twilight Saga: Breaking Dawn Part 2            | Lionsgate
 The Hunger Games: Mockingjay - Part 2              | Lionsgate
 Spider-Man                                         | Sony / Columbia Pictures
 Jumanji: Welcome to the Jungle                     | Sony / Columbia Pictures
 Spider-Man 2                                       | Sony / Columbia Pictures
 Spider-Man 3                                       | Sony / Columbia Pictures
 Spider-Man: Homecoming                             | Sony / Columbia Pictures
 Skyfall                                            | Sony / Columbia Pictures
 The Amazing Spider-Man                             | Sony / Columbia Pictures
 The Lord of the Rings: Return of the King          | New Line Cinema
 The Lord of the Rings: The Two Towers              | New Line Cinema
 The Lord of the Rings: Fellowship of the Ring      | New Line Cinema
 The Passion of the Christ                          | Newmarket Films
 The Twilight Saga: Eclipse                         | Summit Entertainment
 The Twilight Saga: New Moon                        | Summit Entertainment
 The Twilight Saga: Breaking Dawn Part 1            | Summit Entertainment
 Toy Story 3                                        | Walt Disney Studios Motion Pictures
 Iron Man 3                                         | Walt Disney Studios Motion Pictures
 Captain America: Civil War                         | Walt Disney Studios Motion Pictures
 Frozen                                             | Walt Disney Studios Motion Pictures
 Guardians of the Galaxy Vol. 2                     | Walt Disney Studios Motion Pictures
 Finding Nemo                                       | Walt Disney Studios Motion Pictures
 The Jungle Book                                    | Walt Disney Studios Motion Pictures
 Inside Out                                         | Walt Disney Studios Motion Pictures
 Zootopia                                           | Walt Disney Studios Motion Pictures
 Alice in Wonderland                                | Walt Disney Studios Motion Pictures
 Guardians of the Galaxy                            | Walt Disney Studios Motion Pictures
 Thor: Ragnarok                                     | Walt Disney Studios Motion Pictures
: Pictures
 Inside Out                                         | Walt Disney Studios Motion Pictures
 Zootopia                                           | Walt Disney Studios Motion Pictures
 Alice in Wonderland                                | Walt Disney Studios Motion Pictures
 Guardians of the Galaxy                            | Walt Disney Studios Motion Pictures
 Thor: Ragnarok                                     | Walt Disney Studios Motion Pictures
 Pirates of the Caribbean: At World's End           | Walt Disney Studios Motion Pictures
: Pictures
 Inside Out                                         | Walt Disney Studios Motion Pictures
 Zootopia                                           | Walt Disney Studios Motion Pictures
 Alice in Wonderland                                | Walt Disney Studios Motion Pictures
 Guardians of the Galaxy                            | Walt Disney Studios Motion Pictures
 Thor: Ragnarok                                     | Walt Disney Studios Motion Pictures
 Pirates of the Caribbean: At World's End           | Walt Disney Studios Motion Pictures
 Pirates of the Caribbean: Curse of the Black Pearl | Walt Disney Studios Motion Pictures
 The Sixth Sense                                    | Walt Disney Studios Motion Pictures
 Up                                                 | Walt Disney Studios Motion Pictures
 The Chronicles of Narnia: Lion, Witch & Wardrobe   | Walt Disney Studios Motion Pictures
 Monsters, Inc.                                     | Walt Disney Studios Motion Pictures
 Monsters University                                | Walt Disney Studios Motion Pictures
 The Incredibles                                    | Walt Disney Studios Motion Pictures
 Toy Story 2                                        | Walt Disney Studios Motion Pictures
 Harry Potter and the Goblet of Fire                | Warner Bros.
 The Hangover                                       | Warner Bros.
 Gravity                                            | Warner Bros.
 Harry Potter and the Chamber of Secrets            | Warner Bros.

8.  The star first name, star last name, and movie title for every
    matching movie and star pair in the database.
 first_name  |   last_name   |                       title                        
-------------+---------------+----------------------------------------------------
 Frances     | McDormand     | Transformers: Dark of the Moon
 Emma        | Watson        | Beauty and the Beast
 Emma        | Watson        | Harry Potter and the Sorcerer's Stone
 Emma        | Watson        | Harry Potter and the Half-Blood Prince
 Emma        | Watson        | Harry Potter and the Order of the Phoenix
 Emma        | Watson        | Harry Potter and the Goblet of Fire
 Emma        | Watson        | Harry Potter and the Chamber of Secrets
 Emma        | Watson        | Harry Potter and the Deathly Hallows: Part 2
 Emma        | Watson        | Harry Potter and the Deathly Hallows: Part 1
 Daniel      | Radcliffe     | Harry Potter and the Deathly Hallows: Part 2
 Daniel      | Radcliffe     | Harry Potter and the Sorcerer's Stone
 Daniel      | Radcliffe     | Harry Potter and the Half-Blood Prince
 Daniel      | Radcliffe     | Harry Potter and the Deathly Hallows: Part 1
 Daniel      | Radcliffe     | Harry Potter and the Order of the Phoenix
 Daniel      | Radcliffe     | Harry Potter and the Goblet of Fire
 Daniel      | Radcliffe     | Harry Potter and the Chamber of Secrets
 Morgan      | Freeman       | The Dark Knight
 Morgan      | Freeman       | The Dark Knight Rises
 Will        | Smith         | Suicide Squad
 Will        | Smith         | Independence Day
 Cameron     | Diaz          | Shrek 2
 Cameron     | Diaz          | Shrek the Third
 Cameron     | Diaz          | Shrek
 Kate        | Winslet       | Titanic
 Natalie     | Portman       | Star Wars: Episode I - The Phantom Menace
 Natalie     | Portman       | Star Wars: Episode III - Revenge of the Sith
 Natalie     | Portman       | Star Wars: Episode II - Attack of the Clones
 Dwayne      | Johnson       | Jumanji: Welcome to the Jungle
 Dwayne      | Johnson       | Furious 7
 Scarlett    | Johansson     | Marvel's The Avengers
 Scarlett    | Johansson     | Avengers: Age of Ultron
 Scarlett    | Johansson     | Captain America: Civil War
 Scarlett    | Johansson     | The Jungle Book
 Scarlett    | Johansson     | Iron Man 2
 Scarlett    | Johansson     | Sing
 Keira       | Knightley     | Star Wars: Episode I - The Phantom Menace
 Keira       | Knightley     | Pirates of the Caribbean: Dead Man's Chest
 Keira       | Knightley     | Pirates of the Caribbean: At World's End
 Keira       | Knightley     | Pirates of the Caribbean: Curse of the Black Pearl
 Samuel      | Jackson       | Marvel's The Avengers
 Samuel      | Jackson       | Star Wars: Episode I - The Phantom Menace
 Samuel      | Jackson       | Avengers: Age of Ultron
 Samuel      | Jackson       | Jurassic Park
 Samuel      | Jackson       | Star Wars: Episode III - Revenge of the Sith
 Samuel      | Jackson       | Iron Man
 Samuel      | Jackson       | Iron Man 2
 Samuel      | Jackson       | Star Wars: Episode II - Attack of the Clones
 Samuel      | Jackson       | The Incredibles
 Tom         | Hanks         | Toy Story 3
 Tom         | Hanks         | Forrest Gump
 Tom         | Hanks         | Toy Story 2
: Samuel      | Jackson       | Star Wars: Episode I - The Phantom Menace
 Samuel      | Jackson       | Avengers: Age of Ultron
 Samuel      | Jackson       | Jurassic Park
 Samuel      | Jackson       | Star Wars: Episode III - Revenge of the Sith
 Samuel      | Jackson       | Iron Man
 Samuel      | Jackson       | Iron Man 2
 Samuel      | Jackson       | Star Wars: Episode II - Attack of the Clones
 Samuel      | Jackson       | The Incredibles
 Tom         | Hanks         | Toy Story 3
 Tom         | Hanks         | Forrest Gump
 Tom         | Hanks         | Toy Story 2
 Christopher | Plummer       | Up
 Jennifer    | Lawrence      | The Hunger Games: Catching Fire
: Samuel      | Jackson       | Star Wars: Episode I - The Phantom Menace
 Samuel      | Jackson       | Avengers: Age of Ultron
 Samuel      | Jackson       | Jurassic Park
 Samuel      | Jackson       | Star Wars: Episode III - Revenge of the Sith
 Samuel      | Jackson       | Iron Man
 Samuel      | Jackson       | Iron Man 2
 Samuel      | Jackson       | Star Wars: Episode II - Attack of the Clones
 Samuel      | Jackson       | The Incredibles
 Tom         | Hanks         | Toy Story 3
 Tom         | Hanks         | Forrest Gump
 Tom         | Hanks         | Toy Story 2
 Christopher | Plummer       | Up
 Jennifer    | Lawrence      | The Hunger Games: Catching Fire
 Jennifer    | Lawrence      | The Hunger Games
 Jennifer    | Lawrence      | The Hunger Games: Mockingjay - Part 1
 Jennifer    | Lawrence      | The Hunger Games: Mockingjay - Part 2
 Kathy       | Bates         | Titanic
 Harrison    | Ford          | Star Wars: The Force Awakens
 Harrison    | Ford          | Star Wars
 Harrison    | Ford          | Indiana Jones & Kingdom of the Crystal Skull
 Harrison    | Ford          | Return of the Jedi
 Harrison    | Ford          | The Empire Strikes Back
 Viola       | Davis         | Suicide Squad
 Bradley     | Cooper        | Guardians of the Galaxy Vol. 2
 Bradley     | Cooper        | American Sniper
 Bradley     | Cooper        | Guardians of the Galaxy
 Bradley     | Cooper        | The Hangover
 Amy         | Poehler       | Inside Out
 Amy         | Poehler       | Shrek the Third
 Joseph      | Gordon-Levitt | Star Wars: The Last Jedi
 Joseph      | Gordon-Levitt | The Dark Knight Rises
 Joseph      | Gordon-Levitt | Inception
 Danai       | Gurira        | Black Panther
 Angela      | Bassett       | Black Panther
 Ian         | McKellen      | Beauty and the Beast
 Ian         | McKellen      | The Lord of the Rings: Return of the King
 Ian         | McKellen      | The Lord of the Rings: The Two Towers
 Ian         | McKellen      | The Lord of the Rings: Fellowship of the Ring
 Ian         | McKellen      | The Hobbit: An Unexpected Journey
 Maya        | Rudolph       | Shrek the Third
 Jenny       | Slate         | The Secret Life of Pets
 Jenny       | Slate         | Zootopia
 Jenny       | Slate         | Despicable Me 3
 Idris       | Elba          | Finding Dory
 Idris       | Elba          | Avengers: Age of Ultron
 Idris       | Elba          | The Jungle Book
 Idris       | Elba          | Zootopia
 Idris       | Elba          | Thor: Ragnarok
 Octavia     | Spencer       | Spider-Man
 Octavia     | Spencer       | Zootopia
 Chadwick    | Boseman       | Black Panther
 Chadwick    | Boseman       | Captain America: Civil War
 Michael     | Keaton        | Toy Story 3
 Michael     | Keaton        | Minions
 Michael     | Keaton        | Spider-Man: Homecoming
 Kristen     | Wiig          | Despicable Me 2
 Kristen     | Wiig          | Despicable Me 3
 Keanu       | Reeves        | The Matrix Reloaded
 Helena      | Carter        | Harry Potter and the Deathly Hallows: Part 2
 Helena      | Carter        | Alice in Wonderland
 Helena      | Carter        | Harry Potter and the Half-Blood Prince
 Helena      | Carter        | Harry Potter and the Deathly Hallows: Part 1
 Helena      | Carter        | Harry Potter and the Order of the Phoenix
 Daniel      | Craig         | Star Wars: The Force Awakens
 Daniel      | Craig         | Skyfall
 Emma        | Stone         | The Amazing Spider-Man
 Zoe         | Saldana       | Avatar
 Zoe         | Saldana       | Guardians of the Galaxy Vol. 2
 Zoe         | Saldana       | Guardians of the Galaxy
 Zoe         | Saldana       | Pirates of the Caribbean: Curse of the Black Pearl
 Chris       | Pratt         | Jurassic World
 Chris       | Pratt         | Star Wars
 Chris       | Pratt         | Guardians of the Galaxy Vol. 2
 Chris       | Pratt         | Guardians of the Galaxy
 Anne        | Hathaway      | The Dark Knight Rises
 Anne        | Hathaway      | Alice in Wonderland
 Ellen       | DeGeneres     | Finding Dory
 Ellen       | DeGeneres     | Finding Nemo
 Robert      | Downey Jr.    | Marvel's The Avengers
 Robert      | Downey Jr.    | Avengers: Age of Ultron
 Robert      | Downey Jr.    | Iron Man 3
 Robert      | Downey Jr.    | Captain America: Civil War
 Robert      | Downey Jr.    | Spider-Man: Homecoming
 Robert      | Downey Jr.    | Iron Man
 Robert      | Downey Jr.    | Iron Man 2

9.  The first and last names of every star who has been in a G-rated movie. The first and last name should appear only once for each star, even if they are in several G-rated movies. *IMPORTANT NOTE*: it's possible that there can be two *different* actors with the same name, so make sure your solution accounts for that.

 first_name | last_name 
------------+-----------
 Ellen      | DeGeneres
 Michael    | Keaton
 Tom        | Hanks
(3 rows)


10. The first and last names of every star along with the number
    of movies they have been in, in descending order by the number of movies. (Similar to #9, make sure
    that two different actors with the same name are considered separately).
    
 first_name  |   last_name   | movie_count 
-------------+---------------+-------------
 Samuel      | Jackson       |           9
 Emma        | Watson        |           8
 Daniel      | Radcliffe     |           7
 Robert      | Downey Jr.    |           7
 Scarlett    | Johansson     |           6
 Helena      | Carter        |           5
 Idris       | Elba          |           5
 Ian         | McKellen      |           5
 Harrison    | Ford          |           5
 Zoe         | Saldana       |           4
 Bradley     | Cooper        |           4
 Chris       | Pratt         |           4
 Jennifer    | Lawrence      |           4
 Keira       | Knightley     |           4
 Cameron     | Diaz          |           3
 Jenny       | Slate         |           3
 Joseph      | Gordon-Levitt |           3
 Michael     | Keaton        |           3
 Natalie     | Portman       |           3
 Tom         | Hanks         |           3
 Dwayne      | Johnson       |           2
 Daniel      | Craig         |           2
 Chadwick    | Boseman       |           2
 Will        | Smith         |           2
 Amy         | Poehler       |           2
 Kristen     | Wiig          |           2
 Morgan      | Freeman       |           2
 Octavia     | Spencer       |           2
 Anne        | Hathaway      |           2
 Ellen       | DeGeneres     |           2
 Frances     | McDormand     |           1
 Christopher | Plummer       |           1
 Viola       | Davis         |           1
 Danai       | Gurira        |           1
 Kathy       | Bates         |           1
 Keanu       | Reeves        |           1
 Emma        | Stone         |           1
 Angela      | Bassett       |           1
 Maya        | Rudolph       |           1
 Kate        | Winslet       |           1

### The rest of these are bonuses

11. The title of every movie along with the number of stars in
    that movie, in descending order by the number of stars.
    
                       title                        | star_count 
----------------------------------------------------+------------
 Avengers: Age of Ultron                            |          4
 Harry Potter and the Half-Blood Prince             |          3
 The Dark Knight Rises                              |          3
 Black Panther                                      |          3
 Star Wars: Episode I - The Phantom Menace          |          3
 Iron Man 2                                         |          3
 Harry Potter and the Deathly Hallows: Part 1       |          3
 Guardians of the Galaxy                            |          3
 Harry Potter and the Order of the Phoenix          |          3
 Shrek the Third                                    |          3
:----------------------------------------------------+------------
 Avengers: Age of Ultron                            |          4
 Harry Potter and the Half-Blood Prince             |          3
 The Dark Knight Rises                              |          3
 Black Panther                                      |          3
 Star Wars: Episode I - The Phantom Menace          |          3
 Iron Man 2                                         |          3
 Harry Potter and the Deathly Hallows: Part 1       |          3
 Guardians of the Galaxy                            |          3
 Harry Potter and the Order of the Phoenix          |          3
 Shrek the Third                                    |          3
 Captain America: Civil War                         |          3
 Marvel's The Avengers                              |          3
:----------------------------------------------------+------------
 Avengers: Age of Ultron                            |          4
 Harry Potter and the Half-Blood Prince             |          3
 The Dark Knight Rises                              |          3
 Black Panther                                      |          3
 Star Wars: Episode I - The Phantom Menace          |          3
 Iron Man 2                                         |          3
 Harry Potter and the Deathly Hallows: Part 1       |          3
 Guardians of the Galaxy                            |          3
 Harry Potter and the Order of the Phoenix          |          3
 Shrek the Third                                    |          3
 Captain America: Civil War                         |          3
 Marvel's The Avengers                              |          3
 Zootopia                                           |          3
 Guardians of the Galaxy Vol. 2                     |          3
 Harry Potter and the Deathly Hallows: Part 2       |          3
 Star Wars: Episode III - Revenge of the Sith       |          2
 Spider-Man: Homecoming                             |          2
 Star Wars: The Force Awakens                       |          2
 Harry Potter and the Goblet of Fire                |          2
 Harry Potter and the Sorcerer's Stone              |          2
 Alice in Wonderland                                |          2
 Pirates of the Caribbean: Curse of the Black Pearl |          2
 Iron Man                                           |          2
 Despicable Me 3                                    |          2
 Star Wars: Episode II - Attack of the Clones       |          2
 Star Wars                                          |          2
 Titanic                                            |          2
 Suicide Squad                                      |          2
 Finding Dory                                       |          2
 Beauty and the Beast                               |          2
 Toy Story 3                                        |          2
 Harry Potter and the Chamber of Secrets            |          2
 The Jungle Book                                    |          2
 Jurassic World                                     |          1
 Jurassic Park                                      |          1
 Iron Man 3                                         |          1
 The Dark Knight                                    |          1
 Skyfall                                            |          1
 Forrest Gump                                       |          1
 Return of the Jedi                                 |          1
 Shrek                                              |          1
 Pirates of the Caribbean: At World's End           |          1
 The Lord of the Rings: Fellowship of the Ring      |          1
 The Lord of the Rings: Return of the King          |          1
 American Sniper                                    |          1
 Star Wars: The Last Jedi                           |          1
 The Empire Strikes Back                            |          1
 Despicable Me 2                                    |          1
 The Hangover                                       |          1
 The Matrix Reloaded                                |          1
 Toy Story 2                                        |          1
 Independence Day                                   |          1
 Minions                                            |          1
 Avatar                                             |          1
 Shrek 2                                            |          1
 Indiana Jones & Kingdom of the Crystal Skull       |          1
 The Amazing Spider-Man                             |          1
 Transformers: Dark of the Moon                     |          1
 Inside Out                                         |          1
 The Hunger Games: Mockingjay - Part 2              |          1
 The Lord of the Rings: The Two Towers              |          1
 Furious 7                                          |          1
 The Incredibles                                    |          1
 The Secret Life of Pets                            |          1
 Inception                                          |          1
 Spider-Man                                         |          1
 The Hunger Games: Mockingjay - Part 1              |          1
 The Hobbit: An Unexpected Journey                  |          1
 Up                                                 |          1
 Pirates of the Caribbean: Dead Man's Chest         |          1
 The Hunger Games                                   |          1
 Sing                                               |          1
 Jumanji: Welcome to the Jungle                     |          1
 Finding Nemo                                       |          1
 The Hunger Games: Catching Fire                    |          1
 Thor: Ragnarok                                     |          1
 Monsters University                                |          0
 The Passion of the Christ                          |          0
 Monsters, Inc.                                     |          0
 The Twilight Saga: Breaking Dawn Part 1            |          0
 The Lion King                                      |          0
 Man of Steel                                       |          0
 The Twilight Saga: Breaking Dawn Part 2            |          0
 The Sixth Sense                                    |          0
 It                                                 |          0
 Home Alone                                         |          0
 Deadpool                                           |          0
 Meet the Fockers                                   |          0
 The Chronicles of Narnia: Lion, Witch & Wardrobe   |          0
 The Twilight Saga: New Moon                        |          0
 Rogue One: A Star Wars Story                       |          0
 Transformers                                       |          0
 Frozen                                             |          0
 Spider-Man 3                                       |          0
 Wonder Woman                                       |          0
 Batman v Superman: Dawn of Justice                 |          0
 The Twilight Saga: Eclipse                         |          0
 E. T.: The Extra-Terrestrial                       |          0
 Spider-Man 2                                       |          0
 Gravity                                            |          0
 Transformers: Revenge of the Fallen                |          0

12. The first name, last name, and average runtime of the five
    stars whose movies have the longest average.
    
    first_name |   last_name   |   average_runtime    
------------+---------------+----------------------
 Kate       | Winslet       | 194.0000000000000000
 Kathy      | Bates         | 194.0000000000000000
 Ian        | McKellen      | 170.4000000000000000
 Morgan     | Freeman       | 157.5000000000000000
 Joseph     | Gordon-Levitt | 154.6666666666666667

13. The first name, last name, and average runtime of the five
    stars whose movies have the longest average, among stars who have more than one movie in the database.
    
     first_name |   last_name   |   average_runtime    
------------+---------------+----------------------
 Ian        | McKellen      | 170.4000000000000000
 Morgan     | Freeman       | 157.5000000000000000
 Joseph     | Gordon-Levitt | 154.6666666666666667
 Daniel     | Radcliffe     | 148.4285714285714286
 Keira      | Knightley     | 146.7500000000000000

14. The titles of all movies that don't feature any stars in our
    database.
    
    title                       
--------------------------------------------------
 The Lion King
 The Chronicles of Narnia: Lion, Witch & Wardrobe
 Gravity
 E. T.: The Extra-Terrestrial
 Man of Steel
 The Sixth Sense
 It
 Meet the Fockers
 The Passion of the Christ
 The Twilight Saga: Breaking Dawn Part 2
 Transformers: Revenge of the Fallen
 Monsters University
 The Twilight Saga: Breaking Dawn Part 1
 Transformers
 The Twilight Saga: Eclipse
 Frozen
 Deadpool
 Batman v Superman: Dawn of Justice
 Spider-Man 2
 Monsters, Inc.
 Spider-Man 3
 Wonder Woman
 The Twilight Saga: New Moon
 Home Alone
 Rogue One: A Star Wars Story

15. The first and last names of all stars that don't appear in any movies in our database.

 first_name | last_name 
------------+-----------
 Jim        | Carrey
 Charles    | Chaplin
 Sean       | Connery
 Angelina   | Jolie
 Halle      | Berry
 Mila       | Kunis
 Chris      | Rock
 Wesley     | Snipes
 Jamie      | Foxx
 Charlize   | Theron

16. The first names, last names, and titles corresponding to every
    role in the database, along with every movie title that doesn't have a star, and the first and last names of every star not in a movie.
    
    first_name  |   last_name   |                    movie_title                     
-------------+---------------+----------------------------------------------------
 Frances     | McDormand     | Transformers: Dark of the Moon
 Emma        | Watson        | Beauty and the Beast
 Emma        | Watson        | Harry Potter and the Sorcerer's Stone
 Emma        | Watson        | Harry Potter and the Half-Blood Prince
 Emma        | Watson        | Harry Potter and the Order of the Phoenix
 Emma        | Watson        | Harry Potter and the Goblet of Fire
 Emma        | Watson        | Harry Potter and the Chamber of Secrets
 Emma        | Watson        | Harry Potter and the Deathly Hallows: Part 2
 Emma        | Watson        | Harry Potter and the Deathly Hallows: Part 1
 Daniel      | Radcliffe     | Harry Potter and the Deathly Hallows: Part 2
 Daniel      | Radcliffe     | Harry Potter and the Sorcerer's Stone
 Daniel      | Radcliffe     | Harry Potter and the Half-Blood Prince
 Daniel      | Radcliffe     | Harry Potter and the Deathly Hallows: Part 1
 Daniel      | Radcliffe     | Harry Potter and the Order of the Phoenix
 Daniel      | Radcliffe     | Harry Potter and the Goblet of Fire
 Daniel      | Radcliffe     | Harry Potter and the Chamber of Secrets
 Morgan      | Freeman       | The Dark Knight
 Morgan      | Freeman       | The Dark Knight Rises
 Will        | Smith         | Suicide Squad
 Will        | Smith         | Independence Day
 Cameron     | Diaz          | Shrek 2
 Cameron     | Diaz          | Shrek the Third
 Cameron     | Diaz          | Shrek
 Kate        | Winslet       | Titanic
 Natalie     | Portman       | Star Wars: Episode I - The Phantom Menace
 Natalie     | Portman       | Star Wars: Episode III - Revenge of the Sith
 Natalie     | Portman       | Star Wars: Episode II - Attack of the Clones
 Dwayne      | Johnson       | Jumanji: Welcome to the Jungle
 Dwayne      | Johnson       | Furious 7
 Scarlett    | Johansson     | Marvel's The Avengers
 Scarlett    | Johansson     | Avengers: Age of Ultron
 Scarlett    | Johansson     | Captain America: Civil War
 Scarlett    | Johansson     | The Jungle Book
 Scarlett    | Johansson     | Iron Man 2
 Scarlett    | Johansson     | Sing
 Keira       | Knightley     | Star Wars: Episode I - The Phantom Menace
 Keira       | Knightley     | Pirates of the Caribbean: Dead Man's Chest
 Keira       | Knightley     | Pirates of the Caribbean: At World's End
 Keira       | Knightley     | Pirates of the Caribbean: Curse of the Black Pearl
 Samuel      | Jackson       | Marvel's The Avengers
 Samuel      | Jackson       | Star Wars: Episode I - The Phantom Menace
 Samuel      | Jackson       | Avengers: Age of Ultron
 Samuel      | Jackson       | Jurassic Park
 Samuel      | Jackson       | Star Wars: Episode III - Revenge of the Sith
 Samuel      | Jackson       | Iron Man
 Samuel      | Jackson       | Iron Man 2
 Samuel      | Jackson       | Star Wars: Episode II - Attack of the Clones
 Samuel      | Jackson       | The Incredibles
 Tom         | Hanks         | Toy Story 3
 Tom         | Hanks         | Forrest Gump
 Tom         | Hanks         | Toy Story 2
 Christopher | Plummer       | Up
 Jennifer    | Lawrence      | The Hunger Games: Catching Fire
 Jennifer    | Lawrence      | The Hunger Games
 Jennifer    | Lawrence      | The Hunger Games: Mockingjay - Part 1
 Jennifer    | Lawrence      | The Hunger Games: Mockingjay - Part 2
 Kathy       | Bates         | Titanic
 Harrison    | Ford          | Star Wars: The Force Awakens
 Harrison    | Ford          | Star Wars
 Harrison    | Ford          | Indiana Jones & Kingdom of the Crystal Skull
 Harrison    | Ford          | Return of the Jedi
 Harrison    | Ford          | The Empire Strikes Back
 Viola       | Davis         | Suicide Squad
 Bradley     | Cooper        | Guardians of the Galaxy Vol. 2
 Bradley     | Cooper        | American Sniper
 Bradley     | Cooper        | Guardians of the Galaxy
 Bradley     | Cooper        | The Hangover
 Amy         | Poehler       | Inside Out
 Amy         | Poehler       | Shrek the Third
 Joseph      | Gordon-Levitt | Star Wars: The Last Jedi
 Joseph      | Gordon-Levitt | The Dark Knight Rises
 Joseph      | Gordon-Levitt | Inception
 Danai       | Gurira        | Black Panther
 Angela      | Bassett       | Black Panther
 Ian         | McKellen      | Beauty and the Beast
 Ian         | McKellen      | The Lord of the Rings: Return of the King
 Ian         | McKellen      | The Lord of the Rings: The Two Towers
 Ian         | McKellen      | The Lord of the Rings: Fellowship of the Ring
 Ian         | McKellen      | The Hobbit: An Unexpected Journey
 Maya        | Rudolph       | Shrek the Third
 Jenny       | Slate         | The Secret Life of Pets
 Jenny       | Slate         | Zootopia
 Jenny       | Slate         | Despicable Me 3
 Idris       | Elba          | Finding Dory
 Idris       | Elba          | Avengers: Age of Ultron
 Idris       | Elba          | The Jungle Book
 Idris       | Elba          | Zootopia
 Idris       | Elba          | Thor: Ragnarok
 Octavia     | Spencer       | Spider-Man
 Octavia     | Spencer       | Zootopia
 Chadwick    | Boseman       | Black Panther
 Chadwick    | Boseman       | Captain America: Civil War
 Michael     | Keaton        | Toy Story 3
 Michael     | Keaton        | Minions
 Michael     | Keaton        | Spider-Man: Homecoming
 Kristen     | Wiig          | Despicable Me 2
 Kristen     | Wiig          | Despicable Me 3
 Keanu       | Reeves        | The Matrix Reloaded
 Helena      | Carter        | Harry Potter and the Deathly Hallows: Part 2
 Helena      | Carter        | Alice in Wonderland
 Helena      | Carter        | Harry Potter and the Half-Blood Prince
 Helena      | Carter        | Harry Potter and the Deathly Hallows: Part 1
 Helena      | Carter        | Harry Potter and the Order of the Phoenix
 Daniel      | Craig         | Star Wars: The Force Awakens
 Daniel      | Craig         | Skyfall
 Emma        | Stone         | The Amazing Spider-Man
 Zoe         | Saldana       | Avatar
 Zoe         | Saldana       | Guardians of the Galaxy Vol. 2
 Zoe         | Saldana       | Guardians of the Galaxy
 Zoe         | Saldana       | Pirates of the Caribbean: Curse of the Black Pearl
 Chris       | Pratt         | Jurassic World
 Chris       | Pratt         | Star Wars
 Chris       | Pratt         | Guardians of the Galaxy Vol. 2
 Chris       | Pratt         | Guardians of the Galaxy
 Anne        | Hathaway      | The Dark Knight Rises
 Anne        | Hathaway      | Alice in Wonderland
 Ellen       | DeGeneres     | Finding Dory
 Ellen       | DeGeneres     | Finding Nemo
 Robert      | Downey Jr.    | Marvel's The Avengers
 Robert      | Downey Jr.    | Avengers: Age of Ultron
 Robert      | Downey Jr.    | Iron Man 3
 Robert      | Downey Jr.    | Captain America: Civil War
 Robert      | Downey Jr.    | Spider-Man: Homecoming
 Robert      | Downey Jr.    | Iron Man
 Robert      | Downey Jr.    | Iron Man 2
             |               | Rogue One: A Star Wars Story
             |               | The Lion King
             |               | Deadpool
             |               | Home Alone
             |               | Transformers: Revenge of the Fallen
             |               | Transformers
             |               | E. T.: The Extra-Terrestrial
             |               | Meet the Fockers
             |               | Wonder Woman
             |               | Batman v Superman: Dawn of Justice
             |               | It
             |               | Man of Steel
             |               | The Twilight Saga: Breaking Dawn Part 2
             |               | Spider-Man 2
             |               | Spider-Man 3
             |               | The Passion of the Christ
             |               | The Twilight Saga: Eclipse
             |               | The Twilight Saga: New Moon
             |               | The Twilight Saga: Breaking Dawn Part 1
             |               | Frozen
             |               | The Sixth Sense
             |               | The Chronicles of Narnia: Lion, Witch & Wardrobe
             |               | Monsters, Inc.
             |               | Monsters University
             |               | Gravity
 Jim         | Carrey        | 
 Charles     | Chaplin       | 
 Sean        | Connery       | 
 Angelina    | Jolie         | 
 Halle       | Berry         | 
 Mila        | Kunis         | 
 Chris       | Rock          | 
 Wesley      | Snipes        | 
 Jamie       | Foxx          | 
 Charlize    | Theron        |
