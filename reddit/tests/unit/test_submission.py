import pytest
from reddit.api import *


def test_submission_show_defaults():
    query = "DIY"
    submiss_list = get_submissions(query)
    assert len(list(submiss_list)) == 2


def test_submission_show_with_limit():
    query = "DIY"
    limit = 1
    submiss_list = get_submissions(query, limit)
    assert len(list(submiss_list)) == 1


def test_submission_show_wrong_order():
    query = "DIY"
    order = "price"

    with pytest.raises(InvalidOption):
        get_submissions(query, order=order)


def test_submission_show_formalized():
    query = "/r/DIY"
    submis_list = get_submissions(query)
    assert len(list(submis_list)) > 0


def test_submission_show_formalized2():
    query = "r/DIY"
    submis_list = get_submissions(query)
    assert len(list(submis_list)) > 0


def test_submission_show_formalized3():
    query = "/DIY"
    submis_list = get_submissions(query)
    assert len(list(submis_list)) > 0


def test_submission_show_no_children():
    query = "no_children"

    with pytest.raises(SubredditNotFound):
        get_submissions(query)


def test_submission_show_no_domain_in_children():
    query = "no_domain"

    with pytest.raises(SubredditNotFound):
        get_submissions(query)


def test_submission_with_non_default_limit():
    query = "DIY"
    limit = 1
    submiss_list = get_submissions(query, limit)
    assert len(list(submiss_list)) == 1
