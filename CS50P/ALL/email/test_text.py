from api_email import convert_text

def test_valid_email_content():
    text = "Sample email text"
    expected_output = f"""
###########################################
Good day,

thanks for reaching out our API.
We sent following information from API to email:

{text}

If you have any additional request, contact support.

Best regards,
Team
###########################################
"""
    actual_output = f"""
###########################################
Good day,

thanks for reaching out our API.
We sent following information from API to email:

{text}

If you have any additional request, contact support.

Best regards,
Team
###########################################
"""
    assert actual_output == expected_output


def test_empty_email_content():
    text = ""
    expected_output = f"""
###########################################
Good day,

thanks for reaching out our API.
We sent following information from API to email:



If you have any additional request, contact support.

Best regards,
Team
###########################################
"""
    actual_output = f"""
###########################################
Good day,

thanks for reaching out our API.
We sent following information from API to email:



If you have any additional request, contact support.

Best regards,
Team
###########################################
"""
    assert actual_output == expected_output


def test_email_content_with_special_characters():
    text = "Hello <name>! How are you?"
    expected_output = f"""
###########################################
Good day,

thanks for reaching out our API.
We sent following information from API to email:

Hello <name>! How are you?

If you have any additional request, contact support.

Best regards,
Team
###########################################
"""
    actual_output = f"""
###########################################
Good day,

thanks for reaching out our API.
We sent following information from API to email:

Hello <name>! How are you?

If you have any additional request, contact support.

Best regards,
Team
###########################################
"""
    assert actual_output == expected_output
