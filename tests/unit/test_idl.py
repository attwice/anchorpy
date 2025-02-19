import json
from pathlib import Path
from pytest import mark
from anchorpy import Idl, Program
from solana.publickey import PublicKey


@mark.unit
def test_idls() -> None:
    idls = []
    programs = []
    for path in Path("tests/idls/").iterdir():
        with path.open() as f:
            data = json.load(f)
        idl = Idl.from_json(data)
        idls.append(idl)
        program = Program(idl, PublicKey(1))
        programs.append(program)
    assert idls


@mark.unit
def test_jet_enum() -> None:
    path = Path("tests/idls/jet.json")
    with path.open() as f:
        data = json.load(f)
    idl = Idl.from_json(data)
    program = Program(idl, PublicKey(1))
    expired_err = program.type["CacheInvalidError"].Expired
    assert expired_err(msg="hi").msg == "hi"
    assert expired_err._sumtype_attribs[0][1].type == str
