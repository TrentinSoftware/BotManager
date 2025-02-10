import os
import argparse


def create_project():
    parser = argparse.ArgumentParser(description="Cria um novo projeto com a estrutura padrão.")
    parser.add_argument("--name", required=True, help="Nome do projeto")
    args = parser.parse_args()

    project_name = args.name
    os.makedirs(project_name, exist_ok=True)

    structure = [
        "src",
        "tests",
        "configs",
        "logs",
    ]

    for folder in structure:
        os.makedirs(os.path.join(project_name, folder), exist_ok=True)

    with open(os.path.join(project_name, "README.md"), "w") as f:
        f.write(f"# {project_name}\n")

    print(f"Projeto '{project_name}' criado com sucesso!")


if __name__ == "__main__":
    create_project()
