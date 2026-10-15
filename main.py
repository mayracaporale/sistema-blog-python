
from blog.modelos import Blog
from blog.datos import cargar_posts, guardar_posts
from blog.menu import mostrar_menu


def main():
    posts = cargar_posts()
    blog = Blog(posts)

    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            for post in blog.listar_posts():
                print(f"\nID: {post.id}")
                print(f"Título: {post.titulo}")
                print(f"Contenido: {post.contenido}")
                print(f"Autor: {post.autor.nombre}")
                print(f"Etiquetas: {', '.join(post.tags)}")
                print(f"Estado: {post.estado}")

        elif opcion == "2":
            titulo = input("Ingresá el título a buscar: ")
            resultados = blog.buscar_por_titulo(titulo)

            for post in resultados:
                print(f"{post.id} - {post.titulo}")

            if not resultados:
                print("No se encontraron publicaciones.")

        elif opcion == "3":
            tag = input("Ingresá la etiqueta: ")
            resultados = blog.filtrar_por_tag(tag)

            for post in resultados:
                print(f"{post.id} - {post.titulo}")

            if not resultados:
                print("No se encontraron publicaciones.")

        elif opcion == "4":
            titulo = input("Título: ").strip()
            contenido = input("Contenido: ").strip()
            nombre = input("Nombre del autor: ").strip()
            bio = input("Biografía del autor: ").strip()
            etiquetas = input("Etiquetas separadas por comas: ")
            tags = [
                etiqueta.strip()
                for etiqueta in etiquetas.split(",")
                if etiqueta.strip()
            ]

            try:
                from blog.modelos import Autor

                autor = Autor(nombre, bio)
                blog.crear_post(titulo, contenido, autor, tags)
                print("Publicación creada correctamente.")
            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "5":
            for post, valido in blog.validar_posts():
                estado = "Válida" if valido else "Tiene errores"
                print(f"{post.titulo}: {estado}")

        elif opcion == "6":
            guardar_posts(blog.obtener_posts())
            print("Publicaciones guardadas.")

        elif opcion == "7":
            guardar_posts(blog.obtener_posts())
            print("Datos guardados. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intentá nuevamente.")


if __name__ == "__main__":
    main()
