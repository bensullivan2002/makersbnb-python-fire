from playwright.sync_api import Page, expect
import pytest
# Tests for your routes go here

"""
We can render the index page
"""

def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    p_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(p_tag).to_have_text("This is the homepage.")

# """ 
# Once a username and password that is submitted matches with the database
# we should reach the landing page/dashboard at spaces.html
# """

# def test_once_logged_in_riderect_to_spaces(page, test_web_address):
#     page.goto(f"http://{test_web_address}/Login")
    
#     page.click("text='Login'")
    
#     button = page.locator('login-button')
#     expect(button).to_have_text('LOGIN')
#     page.fill("input[name=email]", "ben@gmail.com")
#     page.fill("input[name=password]", "Password123!")

"""
When a user completes a sign up form, they are redirected to the spaces page and are shown a popup which says 'Sign up successful'.
"""

# def test_successful_sign_up_redirects_to_spaces_and_shows_popup(page, test_web_address):
#     page.goto(f"http://{test_web_address}")
#     page.fill("input[name=email]", "ben@gmail.com")
#     page.fill("input[name=password]", "Password123!")
#     page.fill("input[name=confirm_password]", "Password123!")
#     page.fill("input[name=first_name]", "Ben")
#     page.fill("input[name=last_name]", "Sullivan")
#     page.fill("input[name=phone_number]", "07123456789")
#     page.click("input[type=submit]")
#     page.wait_for_navigation()
#     assert page.url == f"http://{test_web_address}/spaces.html"
#     assert page.inner_text("p") == "Sign up successful!"