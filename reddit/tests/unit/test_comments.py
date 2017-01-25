import pytest
import requests

from reddit.api import *


def test_get_comments_with_defaults():
    comments = get_comments("tesla")
    assert len(list(comments)) == 3


def test_get_comments_with_non_default_limit():
    comments = get_comments("tesla", 1)
    assert len(list(comments)) == 1
