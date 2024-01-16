import typer

from xpdf.add_watermark import add_default_watermark, add_watermark_with_output
from xpdf.remove_watermark import RemoveWatermark

# from xpdf.command.app_instance import app

app = typer.Typer()


@app.command()
def add(
    input: str = typer.Argument(..., help="input_file"),
    content: str = typer.Argument(..., help="content"),
    output: str = typer.Option(None, help="output_file"),
) -> None:
    # typer.echo((input_file, content))
    if output:
        add_watermark_with_output(input_file=input, content=content, output=output)
    else:
        # default
        add_default_watermark(input_file=input, content=content)


@app.command()
def remove(
    input: str = typer.Argument(..., help="input_file"),
) -> None:
    remover = RemoveWatermark()
    remover.process_and_save(input)
