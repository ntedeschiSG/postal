from pathlib import Path

import anndata as ad
import pytest
from cleo.application import Application
from cleo.testers.command_tester import CommandTester

from postal.console.command.latent import LatentCommand
import postal.latent

@pytest.fixture()
def tester() -> CommandTester:
    application = Application()
    application.add(LatentCommand())
    command = application.find("latent")
    return CommandTester(command)


@pytest.fixture()
def paths():
    tests = Path("tests")
    data = tests / "data"
    return {"tests": tests, "data": data}


def test_scvi(tester, paths):
    path = paths['data']
    config_file = path / "config.yaml"
    model_dir = path / "outs" / "vae.model"
    if model_dir.exists():
        f = model_dir / "model.pt"
        f.unlink()
        model_dir.rmdir()

    tester.execute(args=f"{config_file}")
