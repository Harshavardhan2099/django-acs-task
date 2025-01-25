### Simple Web Application made using Django Web Framework 
This application allows users to submit their profile information including their name, email, department, project links, and profile image. The submitted data is displayed in a common profile page. 

## Features 
- Cyberpunk themed UI with animations
- User-friendly form with image upload option
- Displays user information in a visually appealing profile card 
- Styled using Bootstrap and custom CSS
- Supports SQLite database by default

## Requirements 
Ensure you have the following installed: 
- Python 3.8+
- Django 4+
- Pip
- Git

## Screenshots
![Screenshot 1](screenshot1)
![Screenshot 2](screenshot2)

## Installation and Setup 
Follow these steps and use those commands to set up and run the project locally: 
### Step 1: Clone the Repository

```bash 
git clone https://github.com/Harshavardhan2099/django-acs-task.git
cd profile_project
```

### Step 2: Create and Activate a Virtual Environment

```bash
# On windows
python -m venv venv
.\venv\Scripts\activate

# On macOS and Linux
source venv/bin/activate
```

### Step 3: Install Dependencies 
Install the required packages from **requirements.txt**

```bash
pip install -r requirements.txt
```

### Step 4: Apply Migrations 

```bash
python manage.py migrate
```

### Step 5: Run the Development Server 

```bash
python manage.py runserver
```

Now, open your favourite browser and visit: http://127.0.0.1:8000

## Usage Guide 
1. Open the application in your browser
2. Fill in the profile form with your details
3. Upload a profile image (supported formats: JPG, PNG)
4. Submit the form to view your personalized profile

## Project Structure
```
profile_project/
│-- media/               # Uploaded profile images
│-- profiles/            # App directory
│   ├── migrations/      # Database migrations
│   ├── templates/       # HTML templates
│   ├── static/          # CSS and JS files
│   ├── forms.py         # Django forms
│   ├── models.py        # Database models
│   ├── urls.py          # App-specific routes
│   ├── views.py         # Business logic
│   ├── admin.py         # Admin panel customization
│-- profile_project/     # Main project directory
│   ├── settings.py      # Project settings
│   ├── urls.py          # Main URL configuration
│   ├── wsgi.py          # WSGI entry point
│   ├── asgi.py          # ASGI entry point
│-- db.sqlite3           # SQLite database (default)
│-- manage.py            # Django management script
│-- requirements.txt     # Python dependencies
│-- README.md            # Project documentation
│-- venv/                # Virtual environment (optional)
```

## License
This project is open-source and available under the MIT License. 

## Contact 
For any queries or contributions, contact: 
- Email: tonyharshavardhan1@gmail.com or 126003105@sastra.ac.in
