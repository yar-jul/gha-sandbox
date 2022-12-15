import typer
import uvicorn

cli = typer.Typer()


@cli.command()
def hello():
    print("Hello World!")


@cli.command()
def run(
        host: str = typer.Option("0.0.0.0", envvar="API_HOST"),
        port: int = typer.Option(8000, envvar="API_PORT"),
        workers: int = typer.Option(4, envvar="API_WORKERS"),
):
    uvicorn.run(
        "api.main:app",
        host=host,
        port=port,
        workers=workers,
    )


if __name__ == "__main__":
    cli()
