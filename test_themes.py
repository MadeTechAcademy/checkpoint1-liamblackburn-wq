from pathlib import Path
from themes import x2, save_duties_to_html

def test_html_created(tmp_path):
    # temp directory unique to each test func
    html = tmp_path / "duties.html" 

    save_duties_to_html(x2, html)

    assert html.exists()

def testIt():
    assert len(x2) > 10
    assert True is True
    