import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

# c.execute('''CREATE TABLE astronauts
#              (picture_url text, first_name text, last_name text, home text, cell text, dob text, email text, street text, city text)''')

c.execute("INSERT INTO astronauts VALUES ('https://randomuser.me/api/portraits/women/11.jpg','Rose','Tyler', 'Earth', '06-57-53-58-93', '1979-02-09 14:51:47', 'claire.meyer@example.com', '5607 avenue du fort-caire', 'pau')")

c.execute("INSERT INTO astronauts VALUES ('https://randomuser.me/api/portraits/women/90.jpg','Zoe','Heriot', 'Space Station W3', '(994)-880-7632', '1995-07-24 03:06:36', 'leona.neal@example.com', '5282 w gray st', 'san mateo')")

c.execute("INSERT INTO astronauts VALUES ('https://randomuser.me/api/portraits/men/74.jpg','Jo','Grant', 'Earth', '(790)-175-4387', '1988-11-21 22:02:28', 'felix.thomas@example.com', '5464 green lane west', 'masterton')")

c.execute("INSERT INTO astronauts VALUES ('https://randomuser.me/api/portraits/women/75.jpg','Leela','null', 'Unspecified', '685-362-717', '1974-12-16 10:07:29', 'jesus.diaz@example.com', '5086 calle de ferraz', 'las palmas de gran canaria')")

c.execute("INSERT INTO astronauts VALUES ('https://randomuser.me/api/portraits/women/72.jpg','Romana','null', 'Gallifrey', '(252)-667-1555', '1969-03-21 04:59:36', 'latife.tuglu@example.com', '8042 bagdat cd', 'kars')")

c.execute("INSERT INTO astronauts VALUES ('https://randomuser.me/api/portraits/women/11.jpg','Clara','Oswald', 'Earth', '081-321-4304', '1969-09-13 21:18:02', 'sophie.henry@example.com', '5261 mill road', 'ballinasloe')")

c.execute("INSERT INTO astronauts VALUES ('https://randomuser.me/api/portraits/men/33.jpg','Adric','null', 'alzarius', '041-967-96-80', '1970-03-29 15:56:59', 'leo.manninen@example.com', '5652 otavalankatu', 'laukaa')")

conn.commit()

conn.close()
