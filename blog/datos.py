
import json
from pathlib import Path

from blog.modelos import Autor, Post


RUTA_JSON = Path(__file__).resolve().parent.parent / "posts.json"


def cargar_posts():
    if not RUTA_JSON.exists():
        return []

    try:
        with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        posts = []

        for dato in datos:
            autor = Autor(
                dato["autor"]["nombre"],
                dato["autor"].get("bio", "")
            )

            post = Post(
                dato["id"],
                dato["titulo"],
                dato["contenido"],
                autor,
                dato["tags"],
                dato["estado"]
            )

            posts.append(post)

        return posts

    except (json.JSONDecodeError, KeyError, TypeError) as error:
        print(f"Error al cargar las publicaciones: {error}")
        return []


def guardar_posts(posts):
    datos = []

    for post in posts:
        datos.append({
            "id": post.id,
            "titulo": post.titulo,
            "contenido": post.contenido,
            "autor": {
                "nombre": post.autor.nombre,
                "bio": post.autor.bio
            },
            "tags": post.tags,
            "estado": post.estado
        })

    with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)
