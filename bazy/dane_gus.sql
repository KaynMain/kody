DROP TABLE IF EXISTS tbMiasta;
CREATE TABLE tbMiasta (
    id_miasta INTEGER PRIMARY KEY AUTOINCREMENT,
    Nazwa_miasta TEXT(30),
    Wojewodztwo TEXT(30)T 
);

DROP TABLE IF EXISTS tbPowierzchnie;
CREATE TABLE tbPowierzchnie (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Powierzchnia_miasta DECIMAL,
    Powierzchnia_terenow_zielonych DECIMAL,
    Data_aktualizacji DATE,
    id_miasta INTEGER,
    FOREIGN KEY (id_miasta) REFERENCES tbMiasta(id_miasta)
);

DROP TABLE IF EXISTS dane_gus;
CREATE TABLE dane_gus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Liczba_mieszkancow INTEGER,
    Liczba_kobiet INTEGER,
    Grupa_wiekowa TEXT(30),
    Data_aktualizacji DATE,
    id_miasta INTEGER,
    FOREIGN KEY (id_miasta) REFERENCES tbMiasta(id_miasta)
);
