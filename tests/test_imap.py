import os
from tsl_email_utils import imap_download


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        msg = "Set the %s environment variable"
        error_msg = msg % var_name
        raise error_msg


def test_imap_parse_messages():

    host = get_env_variable("EMAIL_HOST")
    username = get_env_variable("EMAIL_USERNAME")
    password = get_env_variable("EMAIL_PASSWORD")
    m = imap_download.EMailClient.connect(host,
                                          username,
                                          password, True)

    source = get_env_variable("EMAIL_SOURCE")
    messages = m.fetch_bodies_plain(sent_from=source)

    assert len(messages) > 0
    assert messages[0] == "this is a message"


def test_fetch_messages_with_default_filter():

    host = get_env_variable("EMAIL_HOST")
    username = get_env_variable("EMAIL_USERNAME")
    password = get_env_variable("EMAIL_PASSWORD")
    m = imap_download.EMailClient.connect(host,
                                          username,
                                          password, True)

    source = get_env_variable("EMAIL_SOURCE")
    func = imap_download.default_filter
    messages = m.fetch_messages(func, False, sent_from=source)

    for m in messages:
        assert len(m) == 2