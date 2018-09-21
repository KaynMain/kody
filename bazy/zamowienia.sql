DROP TABLE IF EXISTS tbZamowienia;
CREATE TABLE tbZamowienia (
    Numer_zamowienia INTEGER PRIMARY KEY AUTOINCREMENT,
    Adres_klienta ,
    Wojewodztw
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
