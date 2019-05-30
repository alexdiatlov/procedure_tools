import pytest
try:
    from unittest import mock
except ImportError:
    import mock
import os

from procedure_tools.procedure import main

@pytest.mark.skipif(
    not os.environ.get('HOST') or not os.environ.get('TOKEN'),
    reason='Either HOST or TOKEN env variables not specified'
)
@pytest.mark.parametrize("argv", [
    (["--acceleration", "1000000", "--path", "/api/2.5/", "--data", "aboveThresholdEU"]),
    (["--acceleration", "1000000", "--path", "/api/2.5/", "--data", "aboveThresholdUA"]),
    (["--acceleration", "1000000", "--path", "/api/2.5/", "--data", "aboveThresholdUA.defense"]),
    (["--acceleration", "1000000", "--path", "/api/2.5/", "--data", "belowThreshold"]),
    (["--acceleration", "1000000", "--path", "/api/2.5/", "--data", "closeFrameworkAgreementUA"]),
    (["--acceleration", "1000000", "--path", "/api/2.5/", "--data", "competitiveDialogueEU"]),
    (["--acceleration", "1000000", "--path", "/api/2.5/", "--data", "competitiveDialogueUA"]),
    (["--acceleration", "1000000", "--path", "/api/2.5/", "--data", "esco"]),
    (["--acceleration", "1000000", "--path", "/api/2.5/", "--data", "negotiation"]),
    (["--acceleration", "1000000", "--path", "/api/2.5/", "--data", "negotiation.quick"]),
    (["--acceleration", "1000000", "--path", "/api/2.5/", "--data", "reporting"]),
    (["--acceleration", "1000000", "--path", "/api/2.5/", "--stop", "bid_create_0.json"]),
    (["--acceleration", "1000000", "--path", "/api/2.5/", "--wait", "edr-qualification"]),
])
def test_main(argv):
    host = os.environ.get('HOST')
    token = os.environ.get('TOKEN')

    print("\n\nTest with args: {}\n\n" % ([host, "*" * 32] + argv))

    with mock.patch('sys.argv', ['', host, token] + argv), pytest.raises(SystemExit) as e:
        main()
    assert e.type == SystemExit
    assert e.value.code == 0
