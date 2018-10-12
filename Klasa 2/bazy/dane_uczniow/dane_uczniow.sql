DROP TABLE IF EXISTS nazwiska;
CREATE TABLE nazwiska (
    Nr_ucz INTEGER PRIMARY KEY,
    Nazwisko TEXT,
    Imie1 TEXT, 
    Imie2 TEXT
);

DROP TABLE IF EXISTS dane_osbowe;
CREATE TABLE dane_osbowe (
    Nr_ucz.	INTEGER,
    Dzien INTEGER,
    Miesiac	INTEGER,
    Rok	INTEGER,
    M_urodzenia	TEXT,
    Wojewodztwo TEXT,
    FOREIGN KEY (Nr_ucz) REFERENCES dane_osbowe(Nr_ucz)
);

DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny (
    Nr_ucz. INTEGER,
    Zach. TEXT,
    Rel_Ety INTEGER DEFAULT,
    Jpol INTEGER DEFAULT,
    Jang INTEGER DEFAULT,
    Jniem INTEGER DEFAULT,
    Mat INTEGER DEFAULT,
    Hist INTEGER DEFAULT,
    Geog INTEGER DEFAULT,
    Biol INTEGER DEFAULT,
    Fiz INTEGER DEFAULT,
    Che INTEGER DEFAULT,
    Tech INTEGER DEFAULT,
    Info INTEGER DEFAULT,
    Plas INTEGER DEFAULT,
    PO INTEGER DEFAULT,
    WF TEXT DEFAULT,
    FOREIGN KEY (Nr_ucz) REFERENCES dane_osbowe(Nr_ucz)
);
