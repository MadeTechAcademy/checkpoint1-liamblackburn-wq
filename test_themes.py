from themes import x2, save_duties_to_html

# TDD Criteria
def test_html_created(tmp_path):
    # temp directory unique to each test func
    html = tmp_path / "duties.html" 

    save_duties_to_html(x2, html)

    assert html.exists()

# ATDD Criteria (ensures program meets user expectation)
def test_html_contains_duties(tmp_path):
    html = tmp_path / "duties.html" 

    save_duties_to_html(x2, html)

    content = html.read_text(encoding="utf-8")
    
    assert "<html>" and "</html>" in content
    assert "<ul>" and "</ul>" in content
    assert "<li>" and "</li>" in content 
    assert "Duty" in content

def testIt():
    assert len(x2) > 10
    assert True is True
    