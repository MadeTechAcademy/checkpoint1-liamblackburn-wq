from themes import duties_list, save_duties_to_html, read_html

# TDD Criteria
def test_html_created(tmp_path):
    # temp directory unique to each test func
    html = tmp_path / "duties.html" 

    save_duties_to_html(duties_list, html)

    assert html.exists()

# ATDD Criteria (ensures program meets user expectation)
def test_html_contains_duties(tmp_path):
    html_file = tmp_path / "duties.html" 

    save_duties_to_html(duties_list, html_file)

    content = read_html(html_file)
    
    assert "<html>" and "</html>" in content
    assert "<ul>" and "</ul>" in content
    assert "<li>" and "</li>" in content 
    assert "Duty" in content

# as a user, i want to select the Bootcamp theme and see duties 1, 2, 3, 4 and 13 displayed in a separate html file

def test_themes_array(tmp_path):
    html_file = tmp_path / "bootcamp_duties.html"
    theme_name = duties_list[0]["name"]
    duties = duties_list[0]["duties"]
    content = read_html(html_file)
    assert theme_name in content
    assert duties in content


def testIt():
    assert len(duties_list) == 13

    