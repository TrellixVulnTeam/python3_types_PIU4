from typing import Any

openssl_cnf: str

def test_ca(tmpdir: Any): ...
def responder(test_ca: Any): ...
def ocsp_request_builder(test_ca: Any, tmpdir: Any): ...
