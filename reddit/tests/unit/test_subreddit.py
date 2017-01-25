import pytest
import itertools
from reddit.api import *


def test_search_subreddit():
    query = "funny"
    subreddit_list = search_subreddits(query, 2)
    assert tuple(itertools.islice(subreddit_list, 2)) == ("ch1", "ch2")


def test_search_empty_subreddit():
    with pytest.raises(RedditApiError):
        search_subreddits(query=None)


def test_search_missing_subreddit():
    query = "a"
    with pytest.raises(SubredditNotFound):
        search_subreddits(query)

def test_search_subreddit_with_non_default_limit():
    query = "funny"
    limit = 1
    submiss_list = search_subreddits(query, limit)
    assert len(list(submiss_list)) == 1