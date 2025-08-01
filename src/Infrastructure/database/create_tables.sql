CREATE TABLE livros(
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano_publicacao INTEGER,
    genero TEXT,
    isbn TEXT UNIQUE,
    status_leitura TEXT CHECK(status_leitura IN ('lido', 'não lido', 'lendo')),
    data_adicionado TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
