import re
import shlex

import subprocess
from pytest_bdd import scenario, given, when, then, parsers


@scenario('reddit.feature', 'Search subreddit by name')
def test_search():
    pass


@given('A wonderer open terminal')
def open_terminal(args):
    args_list = shlex.split(args)
    command = ['nosetests', '--with-freshen'] + args_list
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    scc.output, _ = process.communicate()
    scc.status = process.returncode
    scc.output = _normalize_newlines(scc.output)
    scc.output = scc.output.rstrip()
    _extract_time_and_traceback()
    return


@given(parsers.re(r'A wonderer has a question (?P<question>\.*)'), converters=dict(question = str) )
def given_question(question):
    command = 'reddit-cli search ' + question
    return command


@given(parsers.re(r'A wonderer want read subreddit (?P<subreddit>\.*)'), converters=dict(subreddit = str) )
def given_subreddit(question):
    command = 'reddit-cli subreddit' + question
    return command


@given(parsers.re(r'A wonderer want read subreddit (?P<subreddit>\.*) comments'), converters=dict(subreddit = str) )
def given_subreddit(question):
    command = 'reddit-cli submission' + question
    return command


@when('I asked for such subreddit')
def fire_command(command):
    print subprocess.Popen("echo Hello World", shell=True, stdout=subprocess.PIPE).stdout.read()