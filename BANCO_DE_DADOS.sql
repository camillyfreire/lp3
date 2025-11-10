-- Tabela de usuários
CREATE TABLE usuario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Tabela de projetos
CREATE TABLE projeto (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
	descricao VARCHAR(100) NOT NULL
);

-- Tabela de categorias
CREATE TABLE categoria (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

-- Tabela de tarefas
CREATE TABLE tarefa (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(90) NOT NULL,
    descricao TEXT,
    projeto_id INT NOT NULL REFERENCES projeto(id),
    responsavel_id INT NOT NULL REFERENCES usuario(id),
    categoria_id INT NOT NULL REFERENCES categoria(id),
    prioridade VARCHAR(10) NOT NULL,
    status VARCHAR(15) NOT NULL,
    data_criacao DATE NOT NULL,
    prazo DATE NOT NULL
);

-- Usuários
INSERT INTO usuario (nome, email) VALUES 
('João', 'joao@email.com'),
('Maria', 'maria@email.com'),
('Carlos', 'carlos@email.com');

-- Projetos
INSERT INTO projeto (nome,descricao) VALUES 
('Projeto Alpha','teste'),
('Projeto Beta','teste'),
('Projeto Gamma','teste');

-- Categorias
INSERT INTO categoria (nome) VALUES 
('Desenvolvimento'),
('Teste'),
('Documentação');

-- Tarefas de exemplo
INSERT INTO tarefa (titulo, descricao, projeto_id, responsavel_id, categoria_id, prioridade, status, data_criacao, prazo)
VALUES 
('Criar login', 'Desenvolver tela de login', 1, 1, 1, 'MEDIA', 'A_FAZER', CURRENT_DATE, '2025-11-11'),
('Testar funcionalidades', 'Testes unitários e integração', 2, 2, 2, 'ALTA', 'EM_ANDAMENTO', CURRENT_DATE, '2025-12-01');
