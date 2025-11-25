from themes import duties_list, save_duties_to_html, save_theme_to_html, read_html, extract_themes_from_html

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

def test_themes_array(tmp_path):
    html_file = tmp_path / "bootcamp_duties.html"
    theme_name = duties_list[0]["name"]
    duties = duties_list[0]["duties"]

    save_theme_to_html(theme_name, duties, html_file)

    content = read_html(html_file)
    assert theme_name in content
    for duty in duties:
        assert duty in content

def test_theme_extraction_from_html(tmp_path):
    html_file = tmp_path / "duties.html"

    save_duties_to_html(duties_list, html_file)
    
    content = extract_themes_from_html(html_file)


def test_correct_number_of_duties():
    assert len(duties_list[0]["duties"]) == 5
    assert len(duties_list[1]["duties"]) == 3
    assert len(duties_list[2]["duties"]) == 4
    assert len(duties_list[3]["duties"]) == 1
    assert len(duties_list[4]["duties"]) == 1
    assert len(duties_list[5]["duties"]) == 1

    