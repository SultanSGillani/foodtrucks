import pytest
from app import app


@pytest.fixture
def client():
    """
    Create a test client for the Flask application.

    Yields:
        FlaskClient: A test client that can be used to make requests to the Flask application.
    """
    with app.test_client() as client:
        yield client


def test_foodtrucks(client):
    """Test the / endpoint."""
    response = client.get('/')
    assert response.status_code == 200

    # Decode the response data to check the HTML content
    html_content = response.data.decode('utf-8')

    # Print the HTML content for debugging purposes
    print(html_content)

    # Check that the HTML response contains the expected content
    assert 'Food Trucks' in html_content
    assert '<th>Applicant</th>' in html_content
    assert '<th>Facility Type</th>' in html_content
    assert '<th>Food Items</th>' in html_content
    assert '<th>Address</th>' in html_content
    assert '<table id="foodtrucks-table"' in html_content
