import re
from lettuce import world, step
from selenium.common.exceptions import NoSuchElementException
from customer.models import Customer



@step(u'I\'m in the customer section')
def when_i_m_in_the_customer_section(step):
    raw_input('')
    world.browser.get("http://0.0.0.0:9000/customer")



@step(u'I click on "([^"]*)"')
def i_click_on_id(step, element_id):
    raw_input('')
    world.browser.find_element_by_id(element_id).click()


@step(u'I write "([^"]*)" in "([^"]*)"')
def i_write_x_in_field_y(step, value, element_id):
    raw_input('')
    world.browser.find_element_by_id(element_id).clear()
    world.browser.find_element_by_id(element_id).send_keys(value)


@step(u'I expect to see the message "([^"]*)"')
def i_expect_to_see_the_message(step, expected_message):
    raw_input('')
    try:
        src = world.browser.page_source
        text_found = re.search(expected_message, src)
        assert text_found
    except NoSuchElementException:
        assert False, "Message not found on page."


@step(u'the table "([^"]*)" should be:')
def the_table_x_should_be(step, table_id):
    raw_input('')
    html_rows = world.browser.find_element_by_id(table_id).find_elements_by_tag_name('tr')
    i = 1
    for table_value in step.hashes:
        html_table_values = html_rows[i].find_elements_by_tag_name('td')
        for expected in table_value.itervalues():
            assert html_table_values[0].text == expected
            del html_table_values[0]
        i += 1


@step(u'I submit the form "([^"]*)"')
def i_submit_the_form(step, element_id):
    raw_input('')
    world.browser.find_element_by_id(element_id).submit()


@step(ur'are the following Customers in the Database:')
def given_are_the_following_Customers_in_the_Database(step):
    raw_input('')
    try:
        for customer_dict in step.hashes:
            customer = Customer(**customer_dict)
            customer.save()
    except Exception, e:
        assert False, "An Exception was raised"



@step(u"I'm doing nothing")
def i_m_doing_nothing(step):
    pass




