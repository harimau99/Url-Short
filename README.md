# URL-Shortener

[URL shortening](https://en.wikipedia.org/wiki/URL_shortening) is  a Uniform Resource Locator (URL) made substantially shorter and available to direct to the page. 

## How to Run Locally?
### Clone the Repository
```
git clone https://github.com/harimau99/Url-Short
```
### Install Dependencies
The project uses following tech stack:
* Python 2.7
* Django 1.11

To insatll dependencies, run
```
pip install -r requirements.txt
```

### Navigate to the Directory
Navigate to the shrinkurl Directory by following this command
```
cd shrinkurl
```

### Run the Applicaiton
```
python manage.py runserver 8000
```

### Open the WebApp in Browser
Open [http://localhost:8000/home](http://localhost:8000/home)
![Short URL Home Page](https://github.com/harimau99/Url-Short/blob/master/Images/image1.png)

### Shorten URL
Enter a URL in the text box
![Short URL Preview](https://github.com/harimau99/Url-Short/blob/master/Images/image2.png)

After submiting the form, the shortned URL will be generated.
![Short URL Preview](https://github.com/harimau99/Url-Short/blob/master/Images/image3.png)

### Administrator in action
Open [http://localhost:8000/admin](http://localhost:8000/admin)
Username : test
Password : plsplspls1
![Short URL ](https://github.com/harimau99/Url-Short/blob/master/Images/admin.png)
![Short URL ](https://github.com/harimau99/Url-Short/blob/master/Images/admin2.png)
