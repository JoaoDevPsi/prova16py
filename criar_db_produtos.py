import sqlite3

def criar_tabela_produtos():
    conn = sqlite3.connect('meu_banco_de_dados.db')
    
    cursor = conn.cursor()
    
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS Produtos (
        ProdutoID INTEGER PRIMARY KEY AUTOINCREMENT,
        NomeProduto VARCHAR(100) NOT NULL,
        Quantidade INTEGER NOT NULL,
        Preco REAL NOT NULL
    );
    """
    
    dados_iniciais = [
        ('Laptop', 10, 1200.50),
        ('Mouse', 50, 25.00),
        ('Teclado', 20, 75.99)
    ]
    
    try:
        cursor.execute(create_table_sql)
        print("Tabela 'Produtos' criada com sucesso ou já existente.")
        
        cursor.execute("SELECT COUNT(*) FROM Produtos")
        if cursor.fetchone()[0] == 0:
            insert_data_sql = "INSERT INTO Produtos (NomeProduto, Quantidade, Preco) VALUES (?, ?, ?)"
            
            cursor.executemany(insert_data_sql, dados_iniciais)
            
            print("Dados iniciais de produtos inseridos com sucesso.")
        else:
            print("Tabela 'Produtos' já contém dados. Pulando inserção inicial.")
            
        conn.commit()
        
    except sqlite3.Error as e:
        print(f"Erro ao operar no banco de dados: {e}")
        
    finally:
        conn.close()

if __name__ == "__main__":
    criar_tabela_produtos()
