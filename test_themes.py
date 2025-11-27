from themes import duties_list, display_to_gui, save_theme_to_html, read_html, extract_themes_from_html

# TDD Criteria
def test_html_created(tmp_path):
    # temp directory unique to each test func
    html = tmp_path / "duties.html" 

    display_to_gui(duties_list, html)

    assert html.exists()

# ATDD Criteria (ensures program meets user expectation)
def test_html_contains_duties(tmp_path):
    html_file = tmp_path / "duties.html" 

    display_to_gui(duties_list, html_file)

    content = read_html(html_file)
    
    assert "<html>" and "</html>" in content
    assert "<ul>" and "</ul>" in content
    assert "<li>" and "</li>" in content 
    assert "Duty" in content

def test_themes_array(tmp_path):
    theme_name = duties_list[0]["name"]
    duties = duties_list[0]["duties"]

    html_file = tmp_path / f"{theme_name}.html"

    save_theme_to_html(theme_name, duties, html_file)

    content = read_html(html_file)

    assert theme_name in content
    for duty in duties:
        assert duty in content

def test_theme_extraction_from_html(tmp_path):

    html_file = tmp_path / "duties.html"
    display_to_gui(duties_list, html_file)

    themes = extract_themes_from_html(html_file, tmp_path)

    for theme_name, duties in themes.items():
        content = read_html(tmp_path / f"{theme_name}.html")
        assert theme_name in content
        for duty in duties:
            assert duty in content

def test_correct_number_of_duties():
    assert len(duties_list[0]["duties"]) == 5
    assert len(duties_list[1]["duties"]) == 3
    assert len(duties_list[2]["duties"]) == 4
    assert len(duties_list[3]["duties"]) == 1
    assert len(duties_list[4]["duties"]) == 1
    assert len(duties_list[5]["duties"]) == 1
    