from QueryBuilder import QueryBuilder

#padrão fluente (Classe Select)
sql = QueryBuilder.select(["id", "descricao"])\
    .from_table("produto").\
    where("id").\
    lesser_than("11").\
    and_where("descricao").\
    equals("'superman'")

print(sql.command)

#prototype

