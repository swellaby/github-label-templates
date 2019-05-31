from tests.test_utilities import parse_template_yaml_file

contents = parse_template_yaml_file("default.yml")
labels = contents["labels"]


def test_num_labels():
    assert len(labels) == 1


def test_bug_label():
    bug = labels[0]
    assert bug["name"] == "bug"
    assert bug["description"] == "Something isn't working"
    assert bug["color"] == "#d73a4a"
