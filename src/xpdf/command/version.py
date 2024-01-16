import typer

# from xpdf.command.app_instance import app

add_watermark_app = typer.Typer()


@add_watermark_app.command()
def add_watermark(
    input_file: str = typer.Argument(..., help="input_file"),
    content: str = typer.Argument(..., help="content"),
) -> None:
    typer.echo((input_file, content))
