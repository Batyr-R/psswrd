import typer
import pyperclip

from services.checker_logic import password_checker, entropy_estimate
from services.generator_logic import generate_password
from categories.storage import storage_app

app = typer.Typer()

@app.command()
def check(password: str, entropy: bool = False):
    strength, reasons = password_checker(password)
    typer.echo(f"The estimated strength of the password is a {strength}/10")
    if strength != 10:
        typer.echo("Reasons being:")
    for r in reasons:
        typer.echo(r)
    if entropy is True:
        typer.echo(f"Entropy estimation is {entropy_estimate(password)} bits")

@app.command()
def gen(length: int = 16):
    if length < 13:
        typer.echo("Length of over 12 characters is required")
        return
    new_password = generate_password(length)
    typer.echo("New secure password:")
    typer.echo(new_password)
    copy = typer.confirm("Copy to clipboard?")
    if copy is True:
        pyperclip.copy(new_password)
        typer.echo("Copied.")

    return

app.add_typer(storage_app, name="storage")

if __name__ == "__main__":
    app()
