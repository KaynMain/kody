DROP TABLE IF EXISTS nazwiska;
CREATE TABLE nazwiska (
    nr_ucznia INTEGER PRIMARY KEY,
    nazwisko TEXT(30),
    imie1 TEXT(15), 
    imie2 TEXT(15)
);

DROP TABLE IF EXISTS dane_osbowe;
CREATE TABLE dane_osbowe (
    nr_ucznia.	INTEGER,
    dzien INTEGER,
    miesiac	INTEGER,
    rok	INTEGER,
    m_urodzenia	TEXT,
    wojewodztwo TEXT,
    FOREIGN KEY (nr_ucznia) REFERENCES nazwiska(nr_ucznia)
);

DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny (
    nr_ucznia. INTEGER,
    zach. TEXT(15),
    rel_Ety DECIMAL DEFAULT NULL,
    jpol DECIMAL DEFAULT NULL,
    jang DECIMAL DEFAULT NULL,
    jniem DECIMAL DEFAULT NULL,
    mat DECIMAL DEFAULT NULL,
    hist DECIMAL DEFAULT NULL,
    geog DECIMAL DEFAULT NULL,
    biol DECIMAL DEFAULT NULL,
    fiz DECIMAL DEFAULT NULL,
    che DECIMAL DEFAULT NULL,
    tech DECIMAL DEFAULT NULL,
    info DECIMAL DEFAULT NULL,
    plas DECIMAL DEFAULT NULL,
    po DECIMAL DEFAULT NULL,
    wf DECIMAL DEFAULT NULL,
    FOREIGN KEY (nr_ucznia) REFERENCES nazwiska(nr_ucznia)
);
