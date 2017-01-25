Feature: Handle subreddit search, show and comments show
  As a reddit user
  I wish to operate via cli client
  In order to get correct results

Background:
  Given A wonderer open terminal

Scenario: Search subreddit by name
  Given A wonderer has a question "the Ultimate Question of Life"
  When I asked for such subreddit
  Then the following answer returned:
  | title |
  | /r/fourtytwo/    |

Scenario: Show subreddit submissions
  Given A wonderer want read subreddit "Tesla"
  When I asked for such subreddit submission
  Then the following answer returned:
  | title |
  | # See r/TeslaMotors for the company |

Scenario:  Show submissions comments
  Given A wonderer want read subreddit "Tesla" comments
  When I asked for such comments
  Then the following answer returned:
  | title |
  | # His First Wipeout |