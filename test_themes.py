from themes import duties_list, save_duties_to_html

# TDD Criteria
def test_html_created(tmp_path):
    # temp directory unique to each test func
    html = tmp_path / "duties.html" 

    save_duties_to_html(duties_list, html)

    assert html.exists()

# ATDD Criteria (ensures program meets user expectation)
def test_html_contains_duties(tmp_path):
    html = tmp_path / "duties.html" 

    save_duties_to_html(duties_list, html)

    content = html.read_text(encoding="utf-8")
    
    assert "<html>" and "</html>" in content
    assert "<ul>" and "</ul>" in content
    assert "<li>" and "</li>" in content 
    assert "Duty" in content

def testIt():
    assert len(duties_list) == 13
    