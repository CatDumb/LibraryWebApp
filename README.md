# Library Web App

This README provides instructions to install the dependencies required to run the Library Web App.

## Prerequisites

Ensure you have the following installed on your system:
- [Python](https://www.python.org/) (version 3.8 or higher recommended)
- [pip](https://pip.pypa.io/en/stable/) (comes with Python)

## Installation Steps

1. **Clone the Repository**  
    Clone this repository to your local machine:
    ```bash
    git clone https://github.com/your-username/LibraryWebApp.git
    cd LibraryWebApp
    ```

2. **Navigate to the Backend Folder**  
    Change directory to the backend folder:
    ```bash
    cd backend
    ```

3. **Install Dependencies**  
    Run the following command to install all required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**  
    Start the application using Uvicorn:
    ```bash
    uvicorn main:app
    ```
    Replace `app.main:app` with the correct path to your FastAPI application if necessary.

## Additional Notes

- If you encounter issues, ensure your Python and pip versions are up to date.
- Refer to the `requirements.txt` file for a list of all dependencies.

You're now ready to proceed with using the Library Web App!