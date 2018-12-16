from oxwall_site import Oxwall

def test_login_positive(driver,user):

    app = Oxwall(driver)
    app.login_as(user)
    app.wait_until_new_status_appeared
    assert True == app.is_dashbord_page()
    #assert app.is_log ged_in_as(user)