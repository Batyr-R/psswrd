import typer

from services.storage_operations import add_to_storage, update_password, remove_login
from services.generator_logic import generate_password

storage_app = typer.Typer()

@storage_app.command()
def add():
    service = str(input("Service name: "))
    login = str(input("Login: "))
    password = str(input("Password (press Enter to generate): "))
    if password == "":
        password = generate_password(16)
        typer.echo(f"New password: {password}")

    status = add_to_storage(service, login, password)
    if status == "exists":
        typer.echo("This password is already set for this login and service")
        return

    if status == "needs_update":
        update = typer.confirm("Update password?")
        if update:
            update_password(service, login, password)
            typer.echo("Updated.")
        else:
            typer.echo("Skipped.")
        return
    typer.echo("Added.")

@storage_app.command()
def rm(service: str, login: str):
    status = remove_login(service, login)
    if status == "no_login":
        typer.echo("Login not found.")
        return

    if status == "no_service":
        typer.echo("Service not found.")
        return

    if status == "no_file":
        typer.echo("Nothing added to remove yet")
        return
    typer.echo("Removed.")
