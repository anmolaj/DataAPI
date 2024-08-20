# DataAPI
Basic workflow for Data APIs


## Installation & Running the Application

### Local non docker
1. Ensure Python 3.10.11 is installed on your system. 
2. Install the dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python -m uvicorn app.api:app --reload --port 8081
   ```

### Docker commands
1. docker build -t data-api .
2. docker run -p 8081:8081 data-api

## Usage

- FastAPI generates automated doc ui `Swagger Ui` at `http://127.0.0.1:8081/docs` which can be used to explore the endpoints