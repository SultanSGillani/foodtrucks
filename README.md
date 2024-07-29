
# Food Truck App

A Flask application that displays a list of food trucks from an external data source. The application renders the data in an HTML table and provides sorting functionality.

## Installation

### Prerequisites

- Python 3.11.5
- Docker
- Docker Compose (optional, to test using nginx. This uses v2 of Compose, see [here](https://docs.docker.com/compose/gettingstarted/) for more info)

### Setup

1. **Clone the Repository**

```sh
git clone https://github.com/yourusername/foodtrucks.git
cd foodtrucks
```
Install Dependencies

Create a virtual environment and install the required Python packages:

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the Application
### Locally
Run the Flask application:

```sh
flask run
```
Visit http://localhost:5000 in your browser.

## With Docker
Build and run the Docker container:

```sh
docker build -t foodtrucks .
docker run -p 5000:5000 foodtrucks
```
Visit http://localhost:5000 in your browser.

## With Docker Compose
Start the application using Docker Compose:

```sh
docker compose up
```
Visit http://localhost:5000 in your browser.

## Testing
### Locally
Run the tests using pytest:

```sh
pip install -r tests/test_requirements.txt
PYTHONPATH=. pytest
```

## GitHub Actions
GitHub Actions will automatically run tests on push and pull requests as mentioned in .github/workflows/ci.yml. It will be deployed to docker hub once merged to main.

## Production Deployment
Since the docker image is hosted on DockerHub there are many ways to deploy the app. A Kubernetes deployment would need the proper manifest, and a server deployment can be done with nginx. See the compose and nginx file for more details.


## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/SultanSGillani/foodtrucks/blob/main/LICENSE) file for details.
