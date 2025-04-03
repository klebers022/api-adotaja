import oracledb

# Configuração da conexão com o Oracle
def get_conexao():
    try:
        con = oracledb.connect(user="rm557887", password="210106", dsn="oracle.fiap.com.br/orcl")
        return con
    except oracledb.DatabaseError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para inserir um pet no banco
def inserir_pet(pet: dict):
    sql = """
    INSERT INTO pets (nome, porte, idade, tipo, localizacao, descricao, imagem)
    VALUES (:nome, :porte, :idade, :tipo, :localizacao, :descricao, :imagem)
    """
    conexao = get_conexao()
    if conexao:
        try:
            with conexao.cursor() as cur:
                cur.execute(sql, pet)
            conexao.commit()
        except Exception as e:
            print(f"Erro ao inserir pet: {e}")
        finally:
            conexao.close()

# Função para listar todos os pets
def listar_pets():
    sql = "SELECT id, nome, porte, idade, tipo, localizacao, descricao, imagem FROM pets"
    conexao = get_conexao()
    pets = []
    
    if conexao:
        try:
            with conexao.cursor() as cur:
                cur.execute(sql)
                pets = [
                    {
                        "id": row[0], "nome": row[1], "porte": row[2], "idade": row[3],
                        "tipo": row[4], "localizacao": row[5], "descricao": row[6], "imagem": row[7]
                    }
                    for row in cur.fetchall()
                ]
        except Exception as e:
            print(f"Erro ao listar pets: {e}")
        finally:
            conexao.close()
    
    return pets
