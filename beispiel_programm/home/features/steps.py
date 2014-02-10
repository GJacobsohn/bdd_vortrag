from lettuce import world, step


@step(u'I\'m on the homepage')
def when_i_m_on_the_homepage(step):
    world.browser.get("http://0.0.0.0:9000")


@step(u'I expect the browser title to be "([^"]*)"')
def then_i_expect_the_browser_title_to_be_group1(step, expected_browser_title):
    assert expected_browser_title == world.browser.title


